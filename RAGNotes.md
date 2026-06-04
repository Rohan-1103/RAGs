# RAG Fundamentals — Interview Notes + Important Questions

# What is RAG?

## Definition

RAG (Retrieval-Augmented Generation) is an AI architecture that combines:

* Information Retrieval
* Large Language Models (LLMs)

to generate responses using external knowledge sources.

---

## RAG Workflow

```text id="p7s8gh"
User Query
   ↓
Retriever
   ↓
Relevant Documents
   ↓
LLM
   ↓
Final Answer
```

---

## Why is RAG Important?

### Answer

RAG allows LLMs to:

* Access external/up-to-date data
* Reduce hallucinations
* Answer domain-specific questions
* Work with private documents

---

## Interview One-Liner

> "RAG combines retrieval systems with LLMs to generate grounded and context-aware responses."

---

# Why Was RAG Needed?

## Problem 1: Hallucinations

### What are Hallucinations?

Hallucinations occur when LLMs generate:

* Incorrect facts
* Fake information
* Confident but wrong answers

---

## Why Hallucinations Happen?

### Answer

Because LLMs:

* Predict tokens probabilistically
* Do not truly verify facts
* Rely only on training data

---

# Problem 2: Knowledge Cutoff

## Definition

LLMs only know information available during training.

They cannot inherently know:

* Recent events
* Updated company data
* New research papers

---

# How RAG Solves These Problems

## Solution

RAG retrieves:

* Real documents
* Latest data
* External knowledge

before generation.

This grounds the LLM response in factual context.

---

## Interview One-Liner

> "RAG reduces hallucinations and overcomes knowledge cutoff limitations by injecting external retrieved knowledge into the LLM context."

---

# What is Fine-Tuning?

## Definition

Fine-tuning retrains a pre-trained LLM on custom/domain-specific data.

---

## Why Use Fine-Tuning?

### Answer

Used for:

* Domain adaptation
* Style learning
* Specialized tasks
* Behavior customization

---

# RAG vs Fine-Tuning

| Feature                 | RAG                | Fine-Tuning    |
| ----------------------- | ------------------ | -------------- |
| Updates knowledge       | Yes                | No             |
| Requires retraining     | No                 | Yes            |
| Cost                    | Lower              | Higher         |
| Dynamic knowledge       | Excellent          | Limited        |
| Hallucination reduction | Better             | Moderate       |
| Best for                | External knowledge | Behavior/style |

---

## Best Interview Answer

### When to use RAG?

Use RAG for:

* Dynamic knowledge
* External documents
* Enterprise search

### When to use Fine-Tuning?

Use fine-tuning for:

* Tone/style customization
* Task specialization
* Behavioral alignment

---

# Parsing

## What is Parsing?

### Answer

Parsing extracts structured text/data from raw documents.

---

## Purpose

Convert:

* PDFs
* DOCX
* HTML
* CSV

into machine-readable text.

---

## Common Parsers

* PyPDFLoader
* Unstructured
* BeautifulSoup
* OCR parsers

---

## Interview One-Liner

> "Parsing converts raw unstructured documents into processable text for downstream RAG pipelines."

---

# Chunking

## What is Chunking?

### Answer

Chunking splits large documents into smaller manageable text pieces.

---

## Why Needed?

### Answer

Because:

* LLMs have token limits
* Smaller chunks improve retrieval accuracy
* Embeddings work better on focused content

---

# Chunking Strategies

## 1. Fixed Chunking

Split by fixed size.

---

## 2. Recursive Chunking

Split intelligently using:

* Paragraphs
* Sentences
* Tokens

---

## 3. Semantic Chunking

Split based on meaning/context.

---

## Example

```python id="9o7ksc"
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

---

## Interview One-Liner

> "Chunking improves retrieval quality by splitting large documents into semantically meaningful smaller sections."

---

# Embedding

## What are Embeddings?

### Answer

Embeddings are dense numerical vector representations of text capturing semantic meaning.

---

## Why Important?

### Answer

Embeddings enable:

* Semantic search
* Similarity comparison
* Vector retrieval

---

## Example

```text id="6z9t0x"
"King" → [0.21, -0.55, 0.88 ...]
```

---

## Interview One-Liner

> "Embeddings convert text into high-dimensional vectors for semantic understanding and retrieval."

---

# Vector Database

## What is a Vector DB?

### Answer

A vector database stores embeddings and performs fast similarity search.

---

## Popular Vector DBs

* FAISS
* Chroma
* Pinecone
* Weaviate
* Milvus

---

## Why Needed?

### Answer

Because traditional databases cannot efficiently search high-dimensional vectors.

---

## Interview One-Liner

> "Vector databases store embeddings and enable efficient semantic similarity retrieval."

---

# Similarity Search

## What is Similarity Search?

### Answer

Similarity search retrieves documents whose embeddings are closest to the query embedding.

---

## Common Metrics

* Cosine Similarity
* Euclidean Distance
* Dot Product

---

# Workflow

```text id="8fw2iw"
Query
   ↓
Convert to Embedding
   ↓
Compare with Stored Vectors
   ↓
Retrieve Most Similar Chunks
```

---

## Interview One-Liner

> "Similarity search retrieves semantically related documents using vector distance metrics."

---

# Data Ingestion Pipeline

## What is Data Ingestion?

### Answer

The ingestion pipeline prepares documents before retrieval.

---

# Ingestion Workflow

```text id="jl7j0p"
Documents
   ↓
Parsing
   ↓
Chunking
   ↓
Embedding
   ↓
Store in Vector DB
```

---

## Main Components

1. Loaders
2. Parsers
3. Chunkers
4. Embedding Models
5. Vector Database

---

# Data Retrieval Pipeline

## What is Retrieval Pipeline?

### Answer

The retrieval pipeline fetches relevant documents during user querying.

---

# Retrieval Workflow

```text id="m8q1b6"
User Query
   ↓
Embedding
   ↓
Similarity Search
   ↓
Relevant Chunks
   ↓
LLM
   ↓
Final Response
```

---

# Why Retrieval Pipeline Important?

### Answer

It ensures:

* Context grounding
* Accurate answers
* Reduced hallucinations

---

# Chunking Deep Dive — Interview Notes + Most Important Questions

# Chunk Size

## What is Chunk Size?

### Answer

Chunk size defines how much text is included in a single chunk during document splitting.

Usually measured in:

* Characters
* Tokens
* Words

---

# Why is Chunk Size Important?

### Answer

Chunk size directly affects:

* Retrieval quality
* Context preservation
* Embedding quality
* LLM response accuracy

---

# Problems with Small Chunk Size

## Issues

* Loss of context
* Incomplete information
* Poor semantic meaning

---

## Example

```text id="f5n8s4"
Chunk:
"The capital of"

Next Chunk:
"France is Paris"
```

The meaning gets split.

---

# Problems with Large Chunk Size

## Issues

* Noisy retrieval
* Irrelevant information
* Higher token usage
* Lower retrieval precision

---

# How to Select Optimal Chunk Size?

## Best Interview Answer

Optimal chunk size depends on:

1. Document type
2. Use case
3. Embedding model
4. LLM context window
5. Retrieval requirements

---

# General Industry Recommendations

| Use Case            | Recommended Chunk Size |
| ------------------- | ---------------------- |
| FAQs                | 200–400                |
| Technical Docs      | 500–1000               |
| Research Papers     | 800–1500               |
| Conversational Data | 300–600                |

---

# Practical Rule

### Answer

Choose a chunk size that:

* Preserves semantic meaning
* Fits within retrieval context
* Avoids excessive noise

---

# Best Interview One-Liner

> "Optimal chunk size balances semantic completeness with retrieval precision."

---

# Chunk Overlap

## What is Chunk Overlap?

### Answer

Chunk overlap is the repeated shared text between consecutive chunks.

---

## Example

```text id="0zw2kn"
Chunk 1:
"The capital of France is Paris"

Chunk 2:
"France is Paris and it is famous"
```

Shared portion:

```text id="1s4twk"
"France is Paris"
```

---

# Why is Chunk Overlap Needed?

### Answer

Overlap preserves context continuity between chunks.

Without overlap:

* Important sentences may split
* Semantic meaning may break
* Retrieval quality decreases

---

# How to Decide Overlap Amount?

## Best Interview Answer

Overlap depends on:

* Chunk size
* Sentence continuity
* Document complexity

---

# General Rule

| Chunk Size | Recommended Overlap |
| ---------- | ------------------- |
| 300        | 30–50               |
| 500        | 50–100              |
| 1000       | 100–200             |

---

# Industry Practice

A common production setup:

```python id="f4y0w0"
chunk_size = 1000
chunk_overlap = 200
```

---

# Why `chunk_overlap=200`?

## Most Important Interview Question

### Answer

Without overlap, a sentence split across two chunks loses context at both ends.

Overlap ensures:

* Context continuity
* Better semantic retrieval
* Improved answer quality

---

## Best One-Liner

> "Chunk overlap preserves semantic continuity across chunk boundaries."

---

# Why `1 - distance` for Similarity?

## Most Important Interview Question

### Answer

ChromaDB returns cosine distance:

* `0` → identical
* `2` → opposite

Subtracting from 1 converts distance into similarity score.

---

# Formula

```python id="rtce7d"
similarity = 1 - distance
```

---

# Why Important?

### Answer

Similarity scores are easier to interpret:

* Higher value = more similar
* Lower value = less similar

---

# Best Interview One-Liner

> "Converting distance to similarity makes semantic relevance easier to interpret."

---

# Why Use Same Embedding Model for Chunks and Queries?

## Most Important Interview Question

### Answer

Both query and document embeddings must exist in the same vector space for similarity comparison.

Using different embedding models creates incompatible vector representations.

---

# Why Important?

### Answer

Similarity search only works when:

* Vector dimensions align
* Embedding semantics match
* Distance calculations remain meaningful

---

# What Happens with Different Models?

## Issues

* Incorrect retrieval
* Meaningless similarity scores
* Poor semantic matching

---

# Best Interview One-Liner

> "Query and document embeddings must be generated using the same embedding model to ensure valid vector similarity comparisons."

---

# Important Chunking Strategy Questions

# Recursive Chunking

## Why RecursiveCharacterTextSplitter is preferred?

### Answer

Because it preserves semantic structure by splitting hierarchically:

1. Paragraphs
2. Sentences
3. Words

before forcing hard splits.

---

# Semantic Chunking

## What is Semantic Chunking?

### Answer

Semantic chunking splits text based on meaning instead of fixed sizes.

---

## Advantage

Better retrieval quality.

---

# Token-Based Chunking

## Why token-based chunking is important?

### Answer

Because LLMs operate on tokens, not characters.

Token chunking better aligns with:

* Context windows
* Embedding limits

---

# Important Traditional RAG Concepts Commonly Asked in Interviews

# 1. Retriever

## What is a Retriever?

### Answer

A retriever fetches the most relevant document chunks from the vector database based on semantic similarity.

---

## Types

* Similarity Retriever
* MMR Retriever
* MultiQuery Retriever
* Parent Document Retriever

---

## Interview One-Liner

> "Retrievers fetch relevant contextual documents before LLM generation."

---

# 2. Top-K Retrieval

## What is Top-K?

### Answer

Top-K defines how many most relevant chunks are retrieved from the vector database.

---

## Example

```python id="t7o5p0"
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 5}
)
```

---

## Important Tradeoff

| Small K       | Large K                   |
| ------------- | ------------------------- |
| Less noise    | More context              |
| Faster        | Slower                    |
| May miss info | May add irrelevant chunks |

---

# 3. MMR (Maximum Marginal Relevance)

## What is MMR?

### Answer

MMR retrieves documents that are:

* Relevant
* Diverse

instead of highly similar duplicate chunks.

---

## Why Important?

### Answer

Avoids redundant retrieval.

---

## Example

```python id="9s3k3r"
retriever = vectorstore.as_retriever(
    search_type="mmr"
)
```

---

## Interview One-Liner

> "MMR balances relevance and diversity during retrieval."

---

# 4. Metadata Filtering

## What is Metadata Filtering?

### Answer

Filtering retrieved documents based on metadata.

---

## Example Metadata

* Source
* Date
* Department
* Author

---

## Example

```python id="u0pwv9"
filter={"department": "finance"}
```

---

## Why Important?

### Answer

Improves retrieval precision.

---

# 5. Dense vs Sparse Retrieval

# Dense Retrieval

## Definition

Uses embeddings/vector similarity.

---

## Examples

* OpenAI embeddings
* Sentence Transformers

---

# Sparse Retrieval

## Definition

Keyword-based retrieval.

---

## Examples

* BM25
* TF-IDF

---

# Comparison

| Dense                | Sparse              |
| -------------------- | ------------------- |
| Semantic             | Keyword-based       |
| Better understanding | Exact term matching |
| Expensive            | Faster              |

---

## Interview One-Liner

> "Dense retrieval captures semantic meaning, while sparse retrieval focuses on keyword matching."

---

# 6. BM25

## What is BM25?

### Answer

BM25 is a traditional keyword-based ranking algorithm used in information retrieval.

---

## Why Important?

### Answer

Still highly effective for:

* Exact term matching
* Search systems
* Hybrid search

---

# 7. Hybrid Search

## What is Hybrid Search?

### Answer

Hybrid search combines:

* Dense retrieval
* Sparse retrieval

for better retrieval performance.

---

## Why Important?

### Answer

Combines:

* Semantic understanding
* Exact keyword matching

---

## Interview One-Liner

> "Hybrid search combines semantic and keyword retrieval for improved accuracy."

---

# 8. Re-ranking

## What is Re-ranking?

### Answer

Re-ranking reorders retrieved documents using a stronger model after initial retrieval.

---

## Why Needed?

### Answer

Initial vector retrieval may not rank documents perfectly.

---

## Workflow

```text id="d49kp8"
Retriever
   ↓
Top-K Documents
   ↓
Re-ranker
   ↓
Best Ranked Context
```

---

## Interview One-Liner

> "Re-ranking improves retrieval quality by refining document ordering after initial retrieval."

---

# 9. Context Compression

## What is Context Compression?

### Answer

Compressing retrieved documents to keep only relevant information before sending to the LLM.

---

## Why Important?

### Answer

Reduces:

* Token usage
* Noise
* Latency

---

# 10. Retriever-Augmented Prompting

## What is it?

### Answer

Injecting retrieved chunks directly into prompts before generation.

---

## Example

```text id="jlwmv0"
Context:
[Retrieved Chunks]

Question:
What is RAG?
```

---

# 11. Context Window Limitation

## Important Interview Topic

### Answer

LLMs can process only limited tokens at once.

This affects:

* Number of retrieved chunks
* Chunk size
* Prompt engineering

---

# 12. Hallucination Mitigation

## Beyond RAG

### Other Methods

* Grounding
* Verification chains
* Re-ranking
* Citation generation

---

# 13. Semantic Search

## What is Semantic Search?

### Answer

Semantic search retrieves documents based on meaning rather than exact keywords.

---

# 14. Indexing

## What is Indexing?

### Answer

Indexing organizes embeddings for efficient retrieval.

---

## Popular Index Types

* HNSW
* IVF
* Flat Index

---

# 15. ANN (Approximate Nearest Neighbor)

## What is ANN?

### Answer

ANN algorithms speed up vector similarity search in large-scale vector databases.

---

## Why Important?

### Answer

Exact nearest neighbor search becomes very slow at scale.

---

# 16. Cosine Similarity

## What is Cosine Similarity?

### Answer

Measures angular similarity between vectors.

---

## Why Commonly Used?

### Answer

Works well for semantic embeddings.

---

# Formula

\text{Cosine Similarity} = \frac{A \cdot B}{|A||B|}

---

# 17. Retrieval Precision vs Recall

# Precision

## Definition

How many retrieved documents are actually relevant.

---

# Recall

## Definition

How many relevant documents were successfully retrieved.

---

## Tradeoff

| High Precision | High Recall                  |
| -------------- | ---------------------------- |
| Less noise     | More coverage                |
| May miss info  | May retrieve irrelevant docs |

---

# 18. Query Expansion

## What is Query Expansion?

### Answer

Enhancing user queries with related terms for better retrieval.

---

## Example

```text id="mjlwm1"
"AI" → "Artificial Intelligence, Machine Learning"
```

---

# 19. Multi-Query Retrieval

## What is Multi-Query Retrieval?

### Answer

Generating multiple reformulated queries from a single user query.

---

## Why Important?

### Answer

Improves retrieval coverage.

---

# 20. Parent-Child Retrieval

## What is Parent-Child Retrieval?

### Answer

Store small child chunks for retrieval but return larger parent documents for better context.

---

### Chatbot And RAG Evaluation

Retrieval Augmented Generation (RAG) is a technique that enhances Large Language Models (LLMs) by providing them with relevant external knowledge. It has become one of the most widely used approaches for building LLM applications.

This tutorial will show you how to evaluate your RAG applications using LangSmith. You'll learn:

1. How to create test datasets
2. How to run your RAG application on those datasets
3. How to measure your application's performance using different evaluation metrics

#### Overview
A typical RAG evaluation workflow consists of three main steps:

1. Creating a dataset with questions and their expected answers
2. Running your RAG application on those questions
3. Using evaluators to measure how well your application performed, looking at factors like:
 - Answer relevance
 - Answer accuracy
 - Retrieval quality
 
For this tutorial, we'll create and evaluate a bot that answers questions about a few of Lilian Weng's insightful blog posts.