# 12 - Transformers Math, Attention and Advanced Concepts

## Self-Attention

Self-attention determines which tokens matter when processing a token.

Example:

```text
The animal was tired because it ran.
```

"it" should attend strongly to:

```text
animal
```

## Query, Key, Value

Every token becomes:

```text
Q = Query
K = Key
V = Value
```

Mental Model:

```text
Query = What am I looking for?
Key = What do I contain?
Value = What information do I provide?
```

## Attention Formula

```text
Attention(Q,K,V)
=
softmax(QKᵀ / √dk)V
```

Steps:

1. Compute similarity using QKᵀ
2. Scale by √dk
3. Apply softmax
4. Create weighted value combination

## Why Divide by √dk?

Without scaling:

```text
Large Dot Products
 ↓
Extreme Softmax
 ↓
Unstable Training
```

Scaling stabilizes gradients.

## Softmax

Converts attention scores into probabilities.

```text
0.40
0.30
0.20
0.10
```

Sum = 1

## Multi Head Attention

Instead of one attention mechanism:

```text
Head1
Head2
Head3
Head4
```

Different heads learn:

- Syntax
- Semantics
- Entity relationships
- Long-range dependencies

Formula:

```text
MultiHead(Q,K,V)
=
Concat(head1...headh)Wo
```

## Feed Forward Network

Typically:

```text
Linear
 ↓
GELU/ReLU
 ↓
Linear
```

Adds non-linearity.

## Residual Connections

Formula:

```text
Output = Input + Layer(Input)
```

Benefits:

- Stable training
- Deep networks
- Better gradients

## Layer Normalization

Normalizes activations.

Benefits:

- Faster convergence
- Training stability

## Positional Encoding

Transformers do not naturally understand order.

### Sinusoidal Encoding

```text
PE(pos,2i)
=
sin(pos/10000^(2i/d))

PE(pos,2i+1)
=
cos(pos/10000^(2i/d))
```

### Learned Positional Embeddings

Model learns positions during training.

### RoPE

Rotary Positional Embeddings.

Used in:

- Llama
- Qwen
- Mistral

Advantages:

- Long-context performance
- Relative positioning

## Masked Attention

Used in decoder models.

Example:

```text
I love ____
```

Model cannot see future words.

## Causal Language Modeling

Training Objective:

```text
Predict next token
```

Example:

```text
I love machine
```

Predict:

```text
learning
```

## Context Window

Maximum number of tokens visible.

Examples:

```text
4K
32K
128K
1M+
```

## KV Cache

Stores:

```text
Keys
Values
```

Benefits:

- Faster inference
- Avoid recomputation

## Flash Attention

Optimized attention algorithm.

Benefits:

- Faster training
- Lower memory
- Longer contexts

## Mixture of Experts (MoE)

Instead of using whole model:

```text
Router
 ↓
Selected Experts
```

Benefits:

- Larger models
- Lower inference cost

Examples:

- Mixtral
- DeepSeek MoE

## Long Context Challenges

### Quadratic Attention Cost

```text
O(n²)
```

Tokens interact with all tokens.

### Memory Growth

Longer context requires more memory.

### Position Degradation

Model may ignore distant tokens.

## Advanced Interview Questions

1. Explain self-attention mathematically.
2. What are Q, K and V?
3. Why use multiple heads?
4. Why scale by √dk?
5. What is RoPE?
6. What is masked attention?
7. What is causal attention?
8. KV Cache vs Attention?
9. What is Flash Attention?
10. Why is attention O(n²)?
11. How do modern LLMs support long context?
12. What is MoE?
13. BERT attention vs GPT attention?
14. How are embeddings generated?
15. Explain next-token prediction.

## Senior-Level Interview Answer

Transformers rely on self-attention, where each token produces Query, Key, and Value representations. Attention scores are computed using scaled dot-product attention and transformed through softmax to create context-aware representations. Multi-head attention captures different linguistic relationships, while positional encoding provides sequence order. Modern LLMs extend this architecture with RoPE, KV caching, Flash Attention, and Mixture-of-Experts routing to improve long-context performance and scalability.
