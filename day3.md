# Day 3 - Contains Duplicate

## Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**LeetCode:** https://leetcode.com/problems/contains-duplicate/

---

## Approach

For this solution, I used Python's built-in **set** data structure.

A set stores only unique elements. By converting the input array into a set, any duplicate values are automatically removed.

I then compared the size of the original array with the size of the set:

- If the set contains fewer elements than the original array, duplicates exist.
- Otherwise, every element is unique.

This approach is concise, readable, and efficiently detects duplicates.

---

## Algorithm

1. Convert the input array into a set.
2. Compare the length of the original array with the length of the set.
3. If the array length is greater than the set length, return `True`.
4. Otherwise, return `False`.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Creating the set requires traversing all elements once.

- **Space Complexity:** `O(n)`
  - The set may store up to all unique elements.

---

## Solution (Python)

```python
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        s = set(nums)

        if len(nums) > len(s):
            return True
        else:
            return False
```

---

## Key Concepts

- Sets
- Hashing
- Arrays
- Duplicate Detection

---

## What I Learned

- How Python's `set` automatically removes duplicate values.
- How comparing collection sizes can solve certain problems efficiently.
- The importance of choosing the appropriate data structure instead of relying on nested loops.
- How built-in data structures can lead to simpler and more readable solutions.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
