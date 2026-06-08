import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_groq import ChatGroq

from langchain_classic.chains import RetrievalQA

load_dotenv()
# =========================
# INGESTION
# =========================
def load_documents(directory_path):
    documents = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(           # What does this join method do?
                directory_path,
                filename
            )
            loader = TextLoader(file_path)
            documents.extend(loader.load())     # Difference between extend and append
    print(f"Loaded {len(documents)} documents")
    return documents


# =========================
# CHUNKING
# =========================
def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    return chunks


# =========================
# VECTOR STORE
# =========================
def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_groq_db"
    )
    print("Vector store created")
    return vectorstore


# =========================
# RETRIEVAL QA
# =========================
def setup_qa_chain(vectorstore):
    llm = ChatGroq(
        model_name="llama-3.1-8b-instant",
        temperature=0.2
    )
    
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    
    return qa_chain


# =========================
# MAIN
# =========================
def main():
    print("\nLoading documents...")
    documents = load_documents("./data/text_files")

    print("\nChunking documents...")
    chunks = chunk_documents(documents)

    print("\nCreating vector store...")
    vectorstore = create_vector_store(chunks)

    print("\nSetting up QA chain...")
    qa_chain = setup_qa_chain(vectorstore)

    print("\nRAG System Ready!")
    print("Type 'quit' to exit.\n")
    while True:

        query = input("Your Question: ")

        if query.lower() == "quit":
            print("\nGoodbye!")
            break

        try:
            result = qa_chain.invoke({"query": query})

            print("\nAnswer:")
            print(result["result"])

            print("\nSources:")
            for idx, doc in enumerate(result["source_documents"],start=1):  # What does start = 1 mean and why?
                source = doc.metadata.get("source","Unknown")
                print(f"\n{idx}. {source}")
                print(f"Preview: "f"{doc.page_content[:100]}...")
            print("\n" + "-" * 60)
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()