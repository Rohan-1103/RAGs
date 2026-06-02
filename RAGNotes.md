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