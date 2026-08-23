# 10 - RAG and Advanced RAG Complete Guide

## Purpose

This document is a complete interview-focused and production-focused guide to:

- Retrieval Augmented Generation (RAG)
- Vector Search
- BM25
- Hybrid Search
- Semantic Reranking
- Agentic RAG
- Advanced Retrieval Architectures
- RAG Evaluation
- Enterprise RAG Design
- Interview Questions & Answers

---

# What is RAG?

RAG (Retrieval Augmented Generation) is an architecture pattern that combines:

```text
Information Retrieval
+
Large Language Models
```

Instead of relying only on the model's training data:

```text
Question
  ↓
LLM
  ↓
Answer
```

RAG performs:

```text
Question
  ↓
Retriever
  ↓
Relevant Documents
  ↓
LLM
  ↓
Grounded Answer
```

Goal:

- Reduce hallucinations
- Use enterprise knowledge
- Access up-to-date information
- Cite evidence
- Avoid costly retraining

---

# RAG Architecture

```text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Index
    ↓
Retriever
    ↓
Prompt Augmentation
    ↓
LLM
    ↓
Answer
```

---

# RAG Pipeline Deep Dive

## 1. Ingestion

Sources:

- SharePoint
- PDFs
- SQL
- Dataverse
- Wikis
- Websites
- Blob Storage

---

## 2. Chunking

Documents are split into smaller pieces.

### Fixed Chunking

```text
500 chars
100 overlap
```

### Recursive Chunking

```text
Paragraph
 ↓
Sentence
 ↓
Word
```

### Semantic Chunking

Split by meaning.

Example:

```text
Policy Section
Procedure Section
FAQ Section
```

### Chunk Size

Typical:

```text
256
512
1024 tokens
```

Tradeoff:

```text
Too Small
  ↓
Context Lost

Too Large
  ↓
Noise Added
```

---

## 3. Embeddings

An embedding converts text into a vector.

Example:

```text
How do I reset VPN?
```

becomes

```text
[0.12, 0.77, -0.19, ...]
```

Purpose:

```text
Semantic Search
```

instead of

```text
Keyword Matching
```

---

# Vector Search

## Dense Vectors

Dense embeddings typically contain hundreds or thousands of dimensions.

Example:

```text
1536 dimensions
3072 dimensions
```

---

## Similarity Functions

### Cosine Similarity

Most common.

```text
A · B
──────
|A||B|
```

Measures angle between vectors.

Higher:

```text
More Semantically Similar
```

---

### Dot Product

```text
Σ(Ai × Bi)
```

Uses direction and magnitude.

---

### Euclidean Distance

```text
√Σ(Ai-Bi)^2
```

Smaller distance means closer vectors.

---

# Exact KNN

K Nearest Neighbors.

```text
Compare query vector
against every vector.
```

Pros:

```text
100% Recall
Easy Baseline
```

Cons:

```text
Slow at Scale
```

---

# ANN (Approximate Nearest Neighbors)

Most production systems use ANN.

Trade-off:

```text
Tiny Recall Loss
Huge Speed Increase
```

---

# HNSW

Hierarchical Navigable Small Worlds.

Most common ANN algorithm.

Mental model:

```text
Country
  ↓
City
  ↓
Neighborhood
  ↓
House
```

instead of

```text
Checking every house.
```

Important Parameters:

## M

Graph connectivity.

Higher:

```text
Better Recall
More Memory
```

## efConstruction

Index build quality.

Higher:

```text
Better Index
Slower Build
```

## efSearch

Query-time search breadth.

Higher:

```text
Better Recall
Higher Latency
```

---

# IVF

Inverted File Index.

Workflow:

```text
Vectors
  ↓
Clusters
  ↓
Search Nearby Clusters Only
```

Important Parameter:

```text
nprobe
```

Higher:

```text
Better Recall
More Latency
```

---

# Product Quantization (PQ)

Compresses vectors.

Benefits:

```text
Less Memory
Faster Retrieval
```

Trade-off:

```text
Approximation Error
```

---

# BM25

Best Match 25.

The gold standard keyword retrieval algorithm.

Used in:

- Elasticsearch
- Solr
- Azure AI Search
- OpenSearch

BM25 works well for:

```text
Acronyms
IDs
Codes
Exact Document Names
Exact Policies
```

Example:

```text
AFDD
INC12345
Article 7.5
GST_AML_2025
```

---

# BM25 Concepts

## Term Frequency (TF)

How often a query term appears.

Example:

```text
AFDD appears 5 times
```

Higher relevance.

---

## Inverse Document Frequency (IDF)

Rare terms are more valuable.

Example:

```text
policy
```

appears everywhere.

Low value.

```text
AFDD
```

appears rarely.

High value.

---

## Length Normalization

Long documents do not automatically win.

BM25 compensates for document length.

---

# BM25 Parameters

## k1

Controls TF saturation.

Default:

```text
1.2 - 2.0
```

---

## b

Controls document length normalization.

Default:

```text
0.75
```

---

# BM25 Limitations

Query:

```text
How do I cancel my account?
```

Document:

```text
Subscription termination procedure
```

Semantic relation exists.

BM25 may miss it.

---

# Hybrid Search

Best practice in enterprise RAG.

Combines:

```text
BM25
+
Vector Search
```

Why?

```text
BM25
  ↓
Exact Matching

Vector Search
  ↓
Semantic Matching
```

Together:

```text
Higher Recall
Higher Precision
```

---

# Reciprocal Rank Fusion (RRF)

Used to merge:

```text
BM25 Ranking
+
Vector Ranking
```

Formula:

```text
RRF = Σ 1/(k + rank)
```

Important:

```text
Uses ranks
NOT raw scores
```

This avoids:

```text
BM25 score scale
!=
Cosine score scale
```

---

# Semantic Reranking

One of the highest impact improvements.

Pipeline:

```text
Retrieve Top 50
     ↓
Rerank
     ↓
Keep Top 5
```

---

# Cross Encoder Rerankers

Most common semantic reranking approach.

Bi-Encoder:

```text
Query
 ↓
Embedding

Document
 ↓
Embedding
```

Independent encoding.

---

Cross Encoder:

```text
[Query + Document]
        ↓
Transformer
        ↓
Relevance Score
```

Advantages:

```text
More Accurate
Better Precision
```

Disadvantages:

```text
Slower
```

---

# Does Semantic Reranking Use LLMs?

Not necessarily.

Common options:

## Cross Encoder

Most common.

## Semantic Rankers

Specialized ranking models.

## LLM-based Rerankers

Can use GPT-4, Claude, Gemini etc.

Pros:

```text
Strong reasoning
```

Cons:

```text
Expensive
Slow
```

---

# Metadata Filtering

Enterprise RAG depends heavily on metadata.

Examples:

```text
Process Area
Category
Language
Country
Document Type
Security Group
Owner
```

Benefits:

```text
Security
Higher Precision
Lower Token Usage
```

---

# Parent Child Retrieval

Index:

```text
Small Chunks
```

Return:

```text
Larger Parent Sections
```

Benefits:

```text
High Precision
Good Context
```

---

# Maximum Marginal Relevance (MMR)

Balances:

```text
Relevance
+
Diversity
```

Without MMR:

```text
Top 5 Results
= Same Chunk Repeated
```

With MMR:

```text
Relevant
AND
Non-Repetitive
```

---

# Advanced RAG Techniques

---

# Query Rewriting

User Query:

```text
What about previous policy?
```

Expanded Query:

```text
Previous AFDD Policy Clarification
```

---

# Multi Query Retrieval

Agent generates:

```text
Query 1
Query 2
Query 3
```

Retrieve separately.

Merge results.

Improves recall.

---

# HyDE

Hypothetical Document Embeddings.

Workflow:

```text
Question
  ↓
Generate Hypothetical Answer
  ↓
Embed Answer
  ↓
Search Documents
```

Improves retrieval for indirect questions.

---

# Contextual Retrieval

Add document-level understanding to chunks.

Chunk:

```text
Approval required in 5 days
```

Contextualized:

```text
AFDD Approval Process
Approval required in 5 days
```

Improves retrieval quality.

---

# Multi-Hop RAG

Question requires multiple retrievals.

Example:

```text
Find grant owner
  ↓
Find audit report
  ↓
Find recommendations
```

---

# GraphRAG

Uses:

```text
Entities
Relationships
Knowledge Graphs
```

Example:

```text
Pulkit
  ↓
works_on
  ↓
KM 2.0
```

Good for:

```text
Relationship Questions
```

---

# Self RAG

System asks:

```text
Do I have enough information?
```

If not:

```text
Retrieve Again
```

---

# Corrective RAG (CRAG)

Evaluate retrieval.

Decision:

```text
Good Retrieval?

Yes → Continue
No  → Re-search
```

---

# Agentic RAG

Traditional RAG:

```text
Retrieve Once
Answer Once
```

Agentic RAG:

```text
Retrieve
Evaluate
Rewrite Query
Retrieve Again
Use Another Tool
Validate Evidence
Answer
```

Agent becomes retrieval planner.

---

# RAG Failure Modes

## Low Recall

Correct document never retrieved.

---

## Low Precision

Wrong documents retrieved.

---

## Chunking Failures

Answer split across chunks.

---

## Hallucination

Answer unsupported by context.

---

## Context Window Pollution

Too much irrelevant context.

---

# RAG Metrics

## Faithfulness

Supported Answer Claims
/
Total Answer Claims

---

## Context Recall

Retrieved Supported Claims
/
Reference Claims

---

## Context Precision

How relevant are retrieved chunks?

---

## Answer Relevancy

Does answer address the question?

---

## Retrieval Latency

How long retrieval takes.

---

## Cost

Embeddings
+
Retrieval
+
Generation

---

# Top Interview Questions

## Beginner

1. What is RAG?
2. Why use RAG?
3. What are embeddings?
4. What is a vector database?
5. What is chunking?
6. What is chunk overlap?
7. What is Top-K?
8. What is semantic search?
9. What is cosine similarity?
10. What is BM25?

---

## Intermediate

11. BM25 vs Vector Search?
12. What is Hybrid Search?
13. Why use RRF?
14. What is reranking?
15. What is a Cross Encoder?
16. Chunk size selection strategy?
17. Parent-child retrieval?
18. What causes hallucinations in RAG?
19. What is MMR?
20. How do you improve retrieval quality?

---

## Advanced

21. What is HNSW?
22. ANN vs Exact KNN?
23. What is HyDE?
24. What is GraphRAG?
25. What is Multi-Hop RAG?
26. What is Contextual Retrieval?
27. What is Self-RAG?
28. What is Corrective RAG?
29. What is Agentic RAG?
30. Design an enterprise RAG architecture.

---

# Interview Answers (Short Versions)

## What is RAG?

RAG combines information retrieval with LLM generation. It retrieves relevant context from external sources and injects it into the prompt before answer generation.

---

## BM25 vs Vector Search?

BM25 is lexical and works well for exact keywords, IDs, and acronyms. Vector search is semantic and works well for paraphrases and concept matching.

---

## Why Hybrid Search?

Hybrid search combines BM25 and vector search, providing both exact matching and semantic retrieval.

---

## What is HNSW?

HNSW is a graph-based approximate nearest-neighbor algorithm that provides fast vector retrieval with excellent recall-performance tradeoffs.

---

## What is Semantic Reranking?

Semantic reranking is a second-stage ranking step that scores retrieved documents more accurately using cross-encoders or semantic ranking models.

---

## Traditional vs Agentic RAG?

Traditional RAG retrieves once and answers once.

Agentic RAG allows an agent to iteratively retrieve, evaluate evidence, rewrite queries, call tools, and search again until sufficient evidence is found.

---

# Final Mental Model

```text
BM25
  ↓
Exact Words

Dense Retrieval
  ↓
Meaning

Hybrid Search
  ↓
Best of Both

RRF
  ↓
Merge Rankings

Reranker
  ↓
Find Best Evidence

LLM
  ↓
Generate Answer

Agentic RAG
  ↓
Retrieve
Think
Retrieve Again
Answer
```
