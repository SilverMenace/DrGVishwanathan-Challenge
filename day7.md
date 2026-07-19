# Day 7 - 3Sum

## Problem

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`
- `i != k`
- `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must not contain duplicate triplets.

**LeetCode:** https://leetcode.com/problems/3sum/

---

## Approach

I solved this problem by first sorting the array.

After sorting, I fixed one element at a time and used the two-pointer technique to search for the remaining two elements whose sum, together with the fixed element, equals zero.

For each fixed element:

- Initialize two pointers:
  - `left` starting just after the fixed element.
  - `right` starting from the end of the array.
- Calculate the sum of the three elements.
- If the sum is less than zero, move the left pointer forward.
- If the sum is greater than zero, move the right pointer backward.
- If the sum is zero, store the triplet and move both pointers while skipping duplicate values.

Sorting the array allows duplicate triplets to be avoided efficiently.

---

## Algorithm

1. Sort the input array.
2. Traverse the array using index `i`.
3. Skip duplicate values for the fixed element.
4. Initialize `left = i + 1` and `right = n - 1`.
5. Calculate the sum of the three elements.
6. Move the appropriate pointer based on whether the sum is less than, greater than, or equal to zero.
7. When a valid triplet is found, store it and skip duplicate values.
8. Continue until all unique triplets have been found.

---

## Complexity Analysis

- **Time Complexity:** `O(n²)`
  - The array is sorted once, and the two-pointer search is performed for each element.

- **Space Complexity:** `O(1)` *(excluding the output list)*
  - Only a few extra variables are used.

---

## Key Concepts

- Sorting
- Two Pointers
- Array Traversal
- Duplicate Handling

---

## What I Learned

- How sorting simplifies searching for combinations.
- How the two-pointer technique reduces unnecessary comparisons.
- Why skipping duplicate values is essential for returning only unique triplets.
- How combining sorting with two pointers leads to an efficient solution for sum-based array problems.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
