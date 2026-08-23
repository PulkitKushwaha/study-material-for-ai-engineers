# 11 - Transformers Fundamentals

## What is a Transformer?
A Transformer is a neural network architecture introduced in the 2017 paper Attention Is All You Need.

Core innovation:

```text
Self Attention
+
Parallel Processing
```

Transformers replaced RNNs and LSTMs because they:

- Process sequences in parallel
- Learn long-range dependencies
- Scale efficiently
- Train on massive datasets

## Why RNNs Failed at Scale

Problems:

- Sequential processing
- Vanishing gradients
- Poor long-context understanding
- Slow training

## High-Level Transformer Architecture

```text
Input
 ↓
Tokenization
 ↓
Embeddings
 ↓
Positional Encoding
 ↓
Transformer Blocks
 ↓
Output Layer
```

## Transformer Components

### Tokenization
- BPE
- WordPiece
- SentencePiece

### Embeddings
Convert tokens into dense vectors.

### Positional Encoding
Adds word order information.

### Self-Attention
Allows every token to attend to every other token.

### Multi-Head Attention
Multiple attention mechanisms run in parallel.

### Feed Forward Network
Applies non-linear transformations.

### Residual Connections
Improve gradient flow.

### Layer Normalization
Stabilizes training.

## Encoder vs Decoder

### Encoder
Used for understanding.

Examples:
- BERT
- Sentence Transformers

Characteristics:
- Bidirectional attention
- Sees left and right context

### Decoder
Used for generation.

Examples:
- GPT
- Claude
- Llama
- Gemini

Characteristics:
- Causal attention
- Cannot see future tokens

### Encoder-Decoder
Examples:
- T5
- BART
- Original Transformer

Used for:
- Translation
- Summarization
- Sequence-to-sequence tasks

## Transformer Block

```text
Input
 ↓
Multi Head Attention
 ↓
Add & Norm
 ↓
Feed Forward Network
 ↓
Add & Norm
 ↓
Output
```

## Common Model Families

### BERT
Encoder-only.
Great for:
- Classification
- Search
- Embeddings

### GPT
Decoder-only.
Great for:
- Generation
- Chatbots
- Coding assistants

### T5
Encoder-decoder.
Treats everything as text-to-text.

## Why Transformers Power LLMs

- Parallel training
- Massive scale
- Contextual understanding
- Transfer learning
- Strong representation learning

## Interview Questions

1. What is a transformer?
2. Why did transformers replace RNNs?
3. Encoder vs Decoder?
4. GPT vs BERT?
5. Why is positional encoding necessary?
6. What is self-attention?
7. What is multi-head attention?
8. Why do transformers scale so well?
9. What powers ChatGPT?
10. What is causal masking?

## Interview Answer

A transformer is a deep-learning architecture based on self-attention. Unlike RNNs, transformers process tokens in parallel and allow every token to attend to every other token. Modern LLMs such as GPT, Claude, Gemini, and Llama are built on transformer architectures.
