# Hashing LeetCode Roadmap

> Goal:
>
> Build Hashing intuition from scratch.
>
> By the end of this roadmap, you should be able to immediately recognize:
>
> - Duplicate Detection
> - Frequency Counting
> - Complement Lookup
> - Grouping Problems
> - Visited Set Patterns
>
> Questions are arranged in the order they should be solved.
>
> Do NOT jump around randomly.
>
> Follow the sequence.

---

# Hashing Learning Objectives

By the end of this section I should be able to answer:

✅ When should I use a Set?

✅ When should I use a Dictionary?

✅ When should I use Counter?

✅ When should I use defaultdict?

✅ How do I trade memory for speed?

✅ How do I reduce O(n²) solutions into O(n)?

---

# Stage 1: Duplicate & Existence Checking

Difficulty: Easy

Purpose:

Learn Hash Set.

Learn:

```python
seen = set()
```

Master:

```text
Have I seen this before?
```

---

## LC 217 - Contains Duplicate

Difficulty:

Easy

Recognition Signals:

- Duplicate
- Exists
- Seen before

Pattern:

Hash Set

Template:

Duplicate Detection

Key Learning:

A set gives O(1) lookup.

Brute Force:

```python
O(n²)
```

Optimal:

```python
O(n)
```

Status:

⬜

---

## LC 219 - Contains Duplicate II

Difficulty:

Easy

Recognition Signals:

- Duplicate
- Distance constraint

Pattern:

Hash Map

Template:

Value → Index

Key Learning:

Sometimes existence isn't enough.

Need additional information.

Status:

⬜

---

# Stage 2: Frequency Counting

Difficulty: Easy

Purpose:

Learn Counter.

Learn Frequency Maps.

Master:

```text
How many times?
```

---

## LC 242 - Valid Anagram

Difficulty:

Easy

Recognition Signals:

- Character counts
- Frequency comparison

Pattern:

Counter

Template:

Frequency Counting

Key Learning:

```python
Counter(s) == Counter(t)
```

Status:

⬜

---

## LC 387 - First Unique Character In A String

Difficulty:

Easy

Recognition Signals:

- Unique
- Appears once

Pattern:

Frequency Counting

Template:

Counter + Second Pass

Key Learning:

Count first.

Search second.

Status:

⬜

---

## LC 383 - Ransom Note

Difficulty:

Easy

Recognition Signals:

- Character availability
- Required counts

Pattern:

Frequency Comparison

Template:

Counter

Status:

⬜

---

# Stage 3: Complement Lookup

Difficulty: Easy → Medium

Purpose:

Learn one of the most important interview techniques.

Master:

```text
What value am I missing?
```

---

## LC 1 - Two Sum

Difficulty:

Easy

Recognition Signals:

- Pair
- Target
- Sum

Pattern:

Complement Lookup

Template:

Hash Map

Key Learning:

Instead of searching ahead:

Store information from the past.

Status:

⬜

---

## LC 167 - Two Sum II

Difficulty:

Easy

Recognition Signals:

- Pair
- Sorted Array

Pattern:

Actually solves better with:

Two Pointers

Status:

Skip for now.

We revisit later.

---

# Stage 4: Grouping

Difficulty: Medium

Purpose:

Learn:

```python
defaultdict(list)
```

Master:

```text
Same key → Same bucket
```

---

## LC 49 - Group Anagrams

Difficulty:

Medium

Recognition Signals:

- Group
- Similar words

Pattern:

Grouping

Template:

defaultdict(list)

Key Learning:

Create a signature.

Group by signature.

Status:

⬜

---

# Stage 5: Top Frequency Problems

Difficulty: Medium

Purpose:

Combine:

- Counter
- Hashing
- Frequency Logic

Master:

```text
Most common
```

---

## LC 347 - Top K Frequent Elements

Difficulty:

Medium

Recognition Signals:

- Frequency
- Top K

Pattern:

Counter

Later:

Heap

Key Learning:

Many problems combine multiple patterns.

Status:

⬜

---

# Stage 6: Visited Set Pattern

Difficulty: Easy → Medium

Purpose:

Prepare for Graphs.

Master:

```python
visited = set()
```

---

## LC 202 - Happy Number

Difficulty:

Easy

Recognition Signals:

- Repeating process
- Infinite loop

Pattern:

Visited Set

Key Learning:

Track previously seen states.

Status:

⬜

---

# Stage 7: Mixed Hashing Problems

Difficulty: Medium

Purpose:

Combine everything learned.

---

## LC 128 - Longest Consecutive Sequence

Difficulty:

Medium

Recognition Signals:

- Sequence
- Fast lookup

Pattern:

Hash Set

Key Learning:

Hashing can solve surprising problems.

Status:

⬜

---

## LC 560 - Subarray Sum Equals K

Difficulty:

Medium

Recognition Signals:

- Sum
- Target

Pattern:

Hash Map

(Will revisit later with Prefix Sum)

Status:

⬜

---

# Recommended Solving Order

Week 1 Hashing Roadmap

Day 1

- LC 217 Contains Duplicate
- LC 242 Valid Anagram

---

Day 2

- LC 387 First Unique Character
- LC 383 Ransom Note

---

Day 3

- LC 1 Two Sum

---

Day 4

- LC 219 Contains Duplicate II

---

Day 5

- LC 49 Group Anagrams

---

Day 6

- LC 347 Top K Frequent Elements

---

Day 7

- LC 202 Happy Number
- LC 128 Longest Consecutive Sequence

---

# Progress Tracker

## Duplicate Detection

- [ ] LC 217
- [ ] LC 219

---

## Frequency Counting

- [ ] LC 242
- [ ] LC 387
- [ ] LC 383

---

## Complement Lookup

- [ ] LC 1

---

## Grouping

- [ ] LC 49

---

## Frequency Ranking

- [ ] LC 347

---

## Visited States

- [ ] LC 202

---

## Advanced Hashing

- [ ] LC 128
- [ ] LC 560

---

# Hashing Mastery Checklist

I can immediately identify:

- [ ] Duplicate Problems
- [ ] Frequency Problems
- [ ] Pair Sum Problems
- [ ] Grouping Problems
- [ ] Visited Set Problems

I can implement:

- [ ] Set Template
- [ ] Counter Template
- [ ] Hash Map Template
- [ ] defaultdict Template

I can explain:

- [ ] Why Hashing reduces O(n²) to O(n)
- [ ] Set vs Dictionary
- [ ] Counter vs Dictionary
- [ ] defaultdict vs Dictionary

---

# Exit Criteria

Before moving to Two Pointers:

✅ Solve all roadmap questions

✅ Understand every template

✅ Recognize Hashing pattern within 30 seconds

✅ Explain solution without memorization

If those conditions are met:

Proceed to:

03-two-pointers
