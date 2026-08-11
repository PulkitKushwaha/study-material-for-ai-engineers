# Hashing: Python Templates

> The purpose of this document is not to memorize solutions.
>
> The purpose is to memorize reusable patterns.
>
> Many LeetCode problems are simply variations of a few core Hashing templates.
>
> Learn the pattern.
>
> Reuse it everywhere.

---

# Template 1: Duplicate Detection

## Recognition Signals

Question contains:

- Duplicate
- Repeated
- Unique
- Seen before

Examples:

- Contains Duplicate
- Happy Number
- Contains Duplicate II

---

## Generic Template

```python
seen = set()

for item in items:

    if item in seen:
        return True

    seen.add(item)

return False
```

---

## Mental Model

```text
Have I seen this before?
```

If yes:

Return answer immediately.

---

## Time Complexity

```python
O(n)
```

---

## Space Complexity

```python
O(n)
```

---

# Template 2: Frequency Counting

## Recognition Signals

Question contains:

- Frequency
- Count
- Occurrence
- Most common
- Least common

Examples:

- Valid Anagram
- First Unique Character
- Top K Frequent Elements

---

## Generic Template

```python
freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1
```

---

## Example

Input

```python
[1,1,2,3,3,3]
```

Output

```python
{
    1:2,
    2:1,
    3:3
}
```

---

## Time Complexity

```python
O(n)
```

---

# Template 3: Counter Template

Python shortcut for frequency problems.

---

## Generic Template

```python
from collections import Counter

freq = Counter(items)
```

---

## Example

```python
from collections import Counter

s = "banana"

freq = Counter(s)

print(freq)
```

Output

```python
{
    'b':1,
    'a':3,
    'n':2
}
```

---

## Most Useful Operation

```python
freq.most_common(3)
```

Example

```python
[
    ('a', 3),
    ('n', 2),
    ('b', 1)
]
```

---

# Template 4: Complement Lookup

One of the most important interview templates.

Used heavily in:

- Two Sum
- Pair Sum
- Pair Difference

---

## Recognition Signals

Question contains:

- Pair
- Target
- Sum
- Difference

---

## Generic Template

```python
seen = {}

for num in nums:

    needed = target - num

    if needed in seen:
        return [seen[needed], num]

    seen[num] = True
```

---

## Mental Model

```text
Instead of looking for the answer,
store information that may help future elements.
```

---

## Example

Target:

```python
10
```

Current number:

```python
6
```

Needed:

```python
4
```

Ask:

```python
Have I seen 4?
```

---

# Template 5: Index Tracking

Used when interviewer needs position.

---

## Generic Template

```python
lookup = {}

for index, value in enumerate(nums):

    if something_found:
        return lookup[...]

    lookup[value] = index
```

---

## Example

Two Sum

Return:

```python
[index1, index2]
```

instead of values.

---

# Template 6: Grouping Pattern

## Recognition Signals

Question contains:

- Group
- Categorize
- Organize
- Similar items

Examples:

- Group Anagrams
- Group Transactions
- Group By Category

---

## Generic Template

```python
from collections import defaultdict

groups = defaultdict(list)

for item in items:

    key = some_identifier(item)

    groups[key].append(item)
```

---

## Example

```python
from collections import defaultdict

anagrams = defaultdict(list)

for word in words:

    key = "".join(sorted(word))

    anagrams[key].append(word)

return list(anagrams.values())
```

---

## Mental Model

```text
Same key → same bucket.
```

---

# Template 7: Counting While Traversing

Common interview pattern.

---

## Generic Template

```python
count = 0

for item in items:

    if condition:
        count += 1
```

---

## Example

Count distinct values.

Count occurrences.

Count matches.

---

# Template 8: First Unique Element

Very common pattern.

---

## Recognition Signals

Question contains:

- Unique
- Non-repeating
- Appears once

---

## Generic Template

```python
freq = Counter(items)

for item in items:

    if freq[item] == 1:
        return item
```

---

## Mental Model

Pass 1

```text
Count everything
```

Pass 2

```text
Find required member
```

---

# Template 9: Visited Set

Very important.

Appears later in:

- Trees
- Graphs
- BFS
- DFS

Hashing is the foundation.

---

## Generic Template

```python
visited = set()

for node in nodes:

    if node in visited:
        continue

    visited.add(node)
```

---

## Mental Model

```text
Never process the same thing twice.
```

---

# Template 10: Character Frequency Comparison

Used in:

- Valid Anagram
- Permutation In String
- Sliding Window variants

---

## Generic Template

```python
Counter(s1) == Counter(s2)
```

---

## Example

```python
Counter("listen") ==
Counter("silent")
```

Result

```python
True
```

---

# Template Selection Guide

Question Says...

### Duplicate

Use

```python
set()
```

---

### Frequency

Use

```python
Counter()
```

---

### Pair Sum

Use

```python
Hash Map
```

---

### Group Similar Items

Use

```python
defaultdict(list)
```

---

### Need Position

Use

```python
Hash Map
value -> index
```

---

### Unique Element

Use

```python
Counter
```

---

### Track Visited

Use

```python
set()
```

---

# The Hashing Toolbox

## Set

Purpose

```text
Fast existence checking
```

Questions

```text
Have I seen this before?
```

---

## Dictionary

Purpose

```text
Store extra information
```

Questions

```text
How many?
Where?
What value?
```

---

## Counter

Purpose

```text
Frequency counting
```

Questions

```text
How often?
```

---

## defaultdict

Purpose

```text
Grouping
```

Questions

```text
Which items belong together?
```

---

# Interview Strategy

When you read a new question ask:

1. Do I need to remember previous elements?
2. Do I need fast lookup?
3. Am I counting frequencies?
4. Am I finding pairs?
5. Am I grouping items?

If the answer is YES to any of these:

Think Hashing first.

---

# Hashing Mastery Checklist

I can instantly identify:

- [ ] Duplicate Detection
- [ ] Frequency Counting
- [ ] Pair Sum Problems
- [ ] Grouping Problems
- [ ] Unique Element Problems
- [ ] Visited Set Problems

I know when to use:

- [ ] set()
- [ ] dict()
- [ ] Counter()
- [ ] defaultdict()

I can write all templates from memory.

- [ ] Duplicate Template
- [ ] Frequency Template
- [ ] Pair Sum Template
- [ ] Grouping Template
- [ ] Unique Template
