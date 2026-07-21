# Day 9 - Merge Strings Alternately

## Problem

You are given two strings `word1` and `word2`.

Merge the strings by adding letters in alternating order, starting with `word1`. If one string is longer than the other, append the remaining letters to the end of the merged string.

Return the merged string.

**LeetCode:** https://leetcode.com/problems/merge-strings-alternately/

---

## Approach

I solved this problem by first comparing the lengths of both strings.

If one string was longer than the other, I alternated characters from both strings until the shorter string ended. After that, I appended the remaining characters from the longer string.

To build the answer efficiently, I stored the characters in a list and finally joined them into a single string.

---

## Algorithm

1. Find the lengths of both strings.
2. Determine which string is shorter.
3. Traverse both strings together, appending one character from each alternately.
4. Append the remaining characters from the longer string.
5. Join the list of characters into the final string.
6. Return the merged string.

---

## Complexity Analysis

- **Time Complexity:** `O(n + m)`
  - Each character from both strings is processed exactly once.

- **Space Complexity:** `O(n + m)`
  - A list is used to store the merged characters before creating the final string.

---

## Key Concepts

- String Traversal
- List Operations
- Conditional Logic
- String Joining

---

## What I Learned

- How to merge two strings by traversing them simultaneously.
- How comparing string lengths helps handle unequal-sized inputs.
- Why storing characters in a list before joining them is an efficient way to construct strings in Python.
- How breaking a problem into common and remaining cases simplifies the implementation.

---

## Solution (Python)

```python
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        n = len(word1)
        m = len(word2)
        q = []

        if n > m:
            for i in range(m):
                q.append(word1[i])
                q.append(word2[i])
            for i in range(m, n):
                q.append(word1[i])
        else:
            for i in range(n):
                q.append(word1[i])
                q.append(word2[i])
            for i in range(n, m):
                q.append(word2[i])

        return ''.join(q)
```

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
