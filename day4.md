# Day 4 - Median of Two Sorted Arrays

## Problem

Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n`, return the median of the two sorted arrays.

**LeetCode:** https://leetcode.com/problems/median-of-two-sorted-arrays/

---

## Approach

I solved this problem by first merging the two sorted arrays into a single sorted array using the two-pointer technique.

Both pointers start at the beginning of their respective arrays. At each step, I compare the current elements and append the smaller one to a new array, moving the corresponding pointer forward.

Once all elements from one array have been processed, I append the remaining elements from the other array.

After obtaining the merged sorted array, I calculate the median:

- If the total number of elements is odd, the median is the middle element.
- If the total number of elements is even, the median is the average of the two middle elements.

---

## Algorithm

1. Initialize two pointers, one for each array.
2. Compare the current elements of both arrays.
3. Append the smaller element to the merged array.
4. Move the corresponding pointer forward.
5. Repeat until one array is exhausted.
6. Append the remaining elements from the other array.
7. Find the median based on the length of the merged array.
8. Return the result.

---

## Complexity Analysis

- **Time Complexity:** `O(m + n)`
- **Space Complexity:** `O(m + n)`

---

## Key Concepts

- Two Pointers
- Array Merging
- Sorted Arrays
- Median Calculation

---

## What I Learned

- How to merge two sorted arrays while maintaining sorted order.
- How the two-pointer technique simplifies working with sorted data.
- How to calculate the median for both odd and even-sized arrays.
- How breaking a problem into smaller steps leads to a clean and understandable solution.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
