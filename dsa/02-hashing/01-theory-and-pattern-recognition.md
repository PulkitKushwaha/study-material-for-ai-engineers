# Hashing: Theory & Pattern Recognition

> Hashing is one of the most important patterns in coding interviews.
>
> If there is one pattern that teaches you how to trade memory for speed, it is Hashing.
>
> Many beginner solutions start at O(n²).
>
> Many optimal interview solutions reduce that to O(n) using a Hash Map or Hash Set.

---

# Why Hashing Exists

Imagine this problem:

Given an array:

```python
[1, 2, 3, 2]
```

Determine if any duplicate exists.

---

## Brute Force

Compare every pair.

```python
1 vs 2
1 vs 3
1 vs 2

2 vs 3
2 vs 2

...
```

Time Complexity:

```python
O(n²)
```

---

## Better Idea

What if we remembered everything we've seen?

```python
Seen:
1

Seen:
1, 2

Seen:
1, 2, 3
```

Next value:

```python
2
```

Already seen.

Duplicate found.

Time Complexity:

```python
O(n)
```

This is the core idea of Hashing.

---

# The Fundamental Tradeoff

Hashing teaches an important engineering principle:

> Spend a little extra memory to save a lot of time.

Example:

```python
Use:
set()
```

Memory:

```python
O(n)
```

Time:

```python
O(n)
```

instead of:

```python
O(n²)
```

---

# Mental Model

Imagine carrying a notebook.

Whenever you see something:

```python
5
```

You write:

```python
Seen: 5
```

When you encounter:

```python
5
```

again:

You don't search the entire list.

You check the notebook instantly.

That's Hashing.

---

# The Four Major Hashing Patterns

Most Hashing interview questions fall into one of four categories.

---

# Pattern 1: Duplicate Detection

## Recognition Signals

Look for:

- Duplicate
- Repeated
- Distinct
- Unique
- Already Exists

---

## Mental Question

> Have I seen this before?

---

## Immediate Tool

```python
set()
```

---

## Examples

### LC 217

Contains Duplicate

### LC 219

Contains Duplicate II

---

## Recognition Shortcut

Question says:

```text
duplicate
```

Your brain should immediately think:

```python
set()
```

---

# Pattern 2: Frequency Counting

## Recognition Signals

Look for:

- Count
- Frequency
- Occurrence
- Most frequent
- Least frequent

---

## Mental Question

> How many times does each item appear?

---

## Immediate Tool

```python
Counter
```

or

```python
dict
```

---

## Examples

### LC 242

Valid Anagram

### LC 387

First Unique Character

### LC 347

Top K Frequent Elements

---

## Recognition Shortcut

Question says:

```text
frequency
count
```

Think:

```python
Counter()
```

---

# Pattern 3: Complement Lookup

## Recognition Signals

Look for:

- Pair sum
- Target value
- Two numbers
- Needed value

---

## Mental Question

> What number do I need to complete the answer?

---

Example:

```python
target = 10

current = 6
```

Need:

```python
4
```

---

## Immediate Tool

```python
dict
```

---

## Example

### LC 1

Two Sum

---

## Recognition Shortcut

Question says:

```text
find pair
reach target
```

Think:

```text
Needed Value = Target - Current
```

Hash Map.

---

# Pattern 4: Grouping

## Recognition Signals

Look for:

- Group
- Categorize
- Similar items
- Clusters

---

## Mental Question

> Which items belong together?

---

## Immediate Tool

```python
defaultdict(list)
```

---

## Example

### LC 49

Group Anagrams

---

Input:

```python
["eat","tea","tan","ate","nat","bat"]
```

Output:

```python
[
  ["eat","tea","ate"],
  ["tan","nat"],
  ["bat"]
]
```

---

## Recognition Shortcut

Question says:

```text
group
categorize
```

Think:

```python
defaultdict(list)
```

---

# Hash Set vs Hash Map

This is one of the most common beginner confusions.

---

# Hash Set

Stores only values.

Example:

```python
seen = {1,2,3}
```

Questions:

```text
Have I seen this before?
```

Perfect.

---

# Hash Map

Stores key-value pairs.

Example:

```python
{
  "apple": 3,
  "banana": 5
}
```

Questions:

```text
How many?
Where?
When?
```

Perfect.

---

# Quick Rule

Need only existence?

```python
set()
```

Need additional information?

```python
dict()
```

---

# Counter vs Dictionary

Both work.

Example:

Dictionary

```python
freq = {}

for n in nums:
    freq[n] = freq.get(n,0) + 1
```

---

Counter

```python
freq = Counter(nums)
```

Cleaner.

Same concept.

---

# Important Interview Habit

Whenever you see a problem:

Ask:

```text
Can I remember information from previous elements?
```

If answer is:

```text
YES
```

Hashing should immediately enter your mind.

---

# Brute Force vs Hashing

This is another recurring interview pattern.

---

## Brute Force

Usually:

```python
nested loops
```

Complexity:

```python
O(n²)
```

---

## Hashing

Usually:

```python
single pass
```

Complexity:

```python
O(n)
```

---

# Common Beginner Mistakes

## Mistake 1

Using a list for lookup.

Example:

```python
if x in my_list
```

Complexity:

```python
O(n)
```

---

Better:

```python
if x in my_set
```

Complexity:

```python
O(1)
```

---

## Mistake 2

Using a dictionary when a set is enough.

Need:

```text
Exists?
```

Use:

```python
set()
```

Not:

```python
dict()
```

---

## Mistake 3

Not recognizing frequency problems.

Words such as:

```text
count
frequency
occurrence
```

should scream:

```python
Counter()
```

---

# Pattern Recognition Cheat Sheet

Question Contains...

| Signal | Think |
|----------|--------|
| Duplicate | Set |
| Unique | Set |
| Seen Before | Set |
| Frequency | Counter |
| Count | Counter |
| Pair Sum | Hash Map |
| Target Pair | Hash Map |
| Group Similar Items | defaultdict(list) |
| Most Frequent | Counter |
| Common Elements | Set |

---

# Hashing Decision Tree

Question asks:

Duplicate?

↓

Hash Set

---

Question asks:

Frequency?

↓

Counter

---

Question asks:

Find Pair?

↓

Hash Map

---

Question asks:

Group Similar Items?

↓

defaultdict(list)

---

# Real Interview Goal

When an interviewer asks:

"Given an array, determine whether duplicates exist."

You should not think:

```text
What algorithm do I use?
```

You should immediately think:

```text
Duplicate

↓

Hash Set

↓

O(n)
```

This is the pattern-recognition muscle we are training.

Hashing is not about memorizing solutions.

Hashing is about recognizing when remembering information can eliminate unnecessary work.
