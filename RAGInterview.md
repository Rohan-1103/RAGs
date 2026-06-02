# Most Important RAG Interview Questions

## 1. What is RAG?

### Answer

RAG combines document retrieval with LLM generation to provide context-aware and grounded responses.

---

## 2. Why was RAG introduced?

### Answer

To reduce hallucinations and overcome LLM knowledge cutoff limitations.

---

## 3. Difference between RAG and Fine-Tuning?

### Answer

RAG injects external knowledge dynamically, while fine-tuning modifies model weights through retraining.

---

## 4. Why is chunking important in RAG?

### Answer

Chunking improves retrieval accuracy and handles LLM context window limitations.

---

## 5. What are embeddings?

### Answer

Embeddings are vector representations capturing semantic meaning of text.

---

## 6. Why do we need vector databases?

### Answer

Vector databases efficiently store and retrieve embeddings using similarity search.

---

## 7. What is similarity search?

### Answer

Similarity search retrieves semantically closest documents based on embedding distance metrics.

---

## 8. Explain the ingestion pipeline in RAG.

### Answer

Documents are parsed, chunked, embedded, and stored in a vector database.

---

## 9. Explain the retrieval pipeline in RAG.

### Answer

User queries are embedded, matched against vector DB embeddings, and relevant chunks are sent to the LLM.

---

## 10. What causes hallucinations in LLMs?

### Answer

LLMs generate probabilistic outputs without verifying factual correctness.

---

# Best Interview One-Liner

> "RAG enhances LLMs by grounding responses in retrieved external knowledge, reducing hallucinations and enabling dynamic information access."


# Most Important Interview Questions

## 1. What is chunk size?

### Answer

Chunk size defines the amount of text stored in each chunk during document splitting.

---

## 2. How do you select an optimal chunk size?

### Answer

Choose a size that balances semantic completeness with retrieval precision based on document type and use case.

---

## 3. Why is chunk overlap needed?

### Answer

Chunk overlap preserves context continuity across chunk boundaries.

---

## 4. Why is `chunk_overlap=200` commonly used?

### Answer

Because it helps preserve sentence continuity and semantic meaning between adjacent chunks.

---

## 5. Why convert distance to similarity using `1 - distance`?

### Answer

Because vector databases often return distance metrics, and converting them improves interpretability of relevance scores.

---

## 6. Why should the same embedding model be used for documents and queries?

### Answer

Because similarity search requires both vectors to exist in the same semantic vector space.

---

## 7. What happens if chunk size is too small?

### Answer

Important context may break, reducing retrieval quality.

---

## 8. What happens if chunk size is too large?

### Answer

Retrieval becomes noisy and less precise due to excessive irrelevant context.

---

# Best Interview One-Liner

> "Effective chunking is critical in RAG because retrieval quality depends heavily on semantic continuity, optimal chunk sizing, and consistent embeddings."