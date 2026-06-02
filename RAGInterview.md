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

# Most Important Traditional RAG Interview Questions

## 1. Difference between Dense and Sparse Retrieval?

### Answer

Dense retrieval uses embeddings, while sparse retrieval uses keyword matching.

---

## 2. Why use Hybrid Search?

### Answer

To combine semantic understanding with exact keyword matching.

---

## 3. What is MMR?

### Answer

MMR retrieves relevant yet diverse documents to avoid redundancy.

---

## 4. Why is Re-ranking important?

### Answer

Because initial vector retrieval may not optimally rank document relevance.

---

## 5. What is ANN in vector databases?

### Answer

ANN enables fast approximate similarity search at scale.

---

## 6. What is Metadata Filtering?

### Answer

Filtering documents using metadata such as source, department, or date.

---

## 7. What is Top-K retrieval?

### Answer

Top-K determines how many relevant chunks are retrieved from the vector database.

---

## 8. Why is context compression needed?

### Answer

To reduce token usage and remove irrelevant information before generation.

---

# Best Interview One-Liner

> "Production-grade RAG systems rely not just on embeddings and vector search, but also on optimized retrieval strategies like hybrid search, re-ranking, MMR, metadata filtering, and context compression."

# Advanced RAG Interview Questions — Technical & Optimization Focus

# 1. How do you optimize retrieval accuracy in a RAG system?

### Answer

Retrieval accuracy can be improved using:

* Better chunking strategies
* Hybrid search
* Re-ranking
* Metadata filtering
* Query expansion
* High-quality embeddings
* MMR retrieval

---

# 2. How do you reduce hallucinations in RAG?

### Answer

Techniques include:

* Better retrieval quality
* Re-ranking
* Context grounding
* Citation generation
* Context compression
* Lower temperature
* Verification chains

---

# 3. How do you select the best embedding model?

### Answer

Selection depends on:

* Domain specificity
* Embedding dimensions
* Latency
* Cost
* Multilingual support
* Retrieval benchmark performance

---

# 4. Why is chunking one of the most critical parts of RAG?

### Answer

Because poor chunking directly reduces retrieval quality, semantic coherence, and final answer accuracy.

---

# 5. What happens if chunk size is too large?

### Answer

Large chunks:

* Introduce noise
* Reduce retrieval precision
* Increase token usage
* Lower embedding specificity

---

# 6. What happens if chunk size is too small?

### Answer

Small chunks:

* Lose context
* Break semantic continuity
* Reduce answer completeness

---

# 7. How do you optimize chunk size in production systems?

### Answer

Through:

* Empirical testing
* Recall/precision evaluation
* Domain-specific tuning
* Token budget analysis

---

# 8. Why is chunk overlap important?

### Answer

Chunk overlap preserves semantic continuity across chunk boundaries.

---

# 9. What is the tradeoff of increasing chunk overlap?

### Answer

Higher overlap:

* Improves continuity
* But increases redundancy, storage, and token cost

---

# 10. Why should embeddings for queries and documents use the same model?

### Answer

Because similarity search requires vectors to exist in the same semantic vector space.

---

# 11. How do vector databases optimize similarity search?

### Answer

Using ANN (Approximate Nearest Neighbor) indexing algorithms such as:

* HNSW
* IVF
* PQ

---

# 12. What is HNSW?

### Answer

HNSW (Hierarchical Navigable Small World) is a graph-based ANN algorithm for efficient vector similarity search.

---

# 13. Why is ANN preferred over exact nearest neighbor search?

### Answer

Exact search becomes computationally expensive at scale, while ANN provides much faster retrieval with minimal accuracy tradeoff.

---

# 14. How do you reduce latency in a RAG system?

### Answer

Using:

* Smaller embeddings
* Efficient vector indexes
* Caching
* Hybrid retrieval
* Context compression
* Streaming
* Optimized chunk sizes

---

# 15. What is retrieval latency?

### Answer

The time taken to:

* Embed the query
* Search vector DB
* Retrieve relevant chunks

---

# 16. What is re-ranking and why is it important?

### Answer

Re-ranking uses a stronger model to reorder retrieved documents for higher relevance accuracy.

---

# 17. Why use hybrid search instead of only vector search?

### Answer

Vector search captures semantics but may miss exact keywords; hybrid search combines semantic and lexical retrieval.

---

# 18. What is query expansion?

### Answer

Query expansion reformulates or enriches user queries to improve retrieval coverage.

---

# 19. What is MultiQuery Retrieval?

### Answer

Generating multiple query variations from a single query to improve recall.

---

# 20. Difference between Precision and Recall in RAG?

### Answer

* Precision:
  Relevant retrieved docs / total retrieved docs

* Recall:
  Relevant retrieved docs / all relevant docs available

---

# 21. Why is recall important in RAG?

### Answer

Missing relevant documents can cause the LLM to generate incomplete or hallucinated answers.

---

# 22. Why is precision important in RAG?

### Answer

Low precision introduces noisy irrelevant context that confuses the LLM.

---

# 23. What causes noisy retrieval?

### Answer

* Large chunks
* Poor embeddings
* Bad indexing
* Weak similarity metrics
* Missing metadata filters

---

# 24. Why is metadata filtering important?

### Answer

It narrows retrieval space and improves retrieval precision.

---

# 25. What is context compression?

### Answer

Reducing retrieved context to only the most relevant information before generation.

---

# 26. Why is context compression important?

### Answer

It reduces:

* Token costs
* Latency
* Context window overflow
* Irrelevant information

---

# 27. What is Top-K optimization?

### Answer

Choosing the optimal number of retrieved chunks to balance:

* Coverage
* Noise
* Token usage

---

# 28. Why can large Top-K values hurt performance?

### Answer

Because excessive context introduces irrelevant information and increases token consumption.

---

# 29. What is embedding drift?

### Answer

Embedding drift occurs when embedding distributions change due to:

* Model changes
* Data evolution
* Different embedding providers

---

# 30. Why is caching important in RAG?

### Answer

Caching reduces:

* Embedding recomputation
* Retrieval latency
* API costs

---

# 31. What are common RAG evaluation metrics?

### Answer

* Precision
* Recall
* MRR
* Hit Rate
* Faithfulness
* Answer Relevancy

---

# 32. What is Faithfulness in RAG evaluation?

### Answer

Faithfulness measures whether the generated answer is grounded in retrieved documents.

---

# 33. What is semantic drift in retrieval?

### Answer

Semantic drift occurs when retrieved chunks gradually deviate from the actual user intent.

---

# 34. Why are re-rankers often cross-encoders?

### Answer

Cross-encoders jointly process query-document pairs, producing more accurate relevance scoring.

---

# 35. What is the main bottleneck in large-scale RAG systems?

### Answer

Common bottlenecks:

* Retrieval latency
* Embedding generation
* Token limits
* Context management

---

# 36. How do you optimize token usage in RAG?

### Answer

Using:

* Context compression
* Better chunking
* Smaller Top-K
* Summarization
* Selective retrieval

---

# 37. Why is cosine similarity commonly used?

### Answer

Because cosine similarity measures semantic orientation rather than vector magnitude.

---

# 38. How do you evaluate chunking quality?

### Answer

By measuring:

* Retrieval relevance
* Recall
* Context completeness
* Downstream answer accuracy

---

# 39. Why do production RAG systems use pipelines?

### Answer

Pipelines modularize:

* Ingestion
* Retrieval
* Re-ranking
* Generation
* Evaluation

for scalability and maintainability.

---

# 40. What is the biggest misconception about RAG?

### Answer

That vector search alone guarantees good answers.

In reality, retrieval quality, chunking, re-ranking, and prompt grounding are equally important.

---

# Best Advanced Interview One-Liner

> "High-quality RAG systems depend more on retrieval optimization, chunking strategy, ranking quality, and context engineering than on the LLM itself."
