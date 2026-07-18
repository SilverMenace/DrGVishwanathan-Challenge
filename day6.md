# Day 6 - Can Place Flowers

## Problem

You have a flowerbed represented as an array containing `0`s and `1`s, where:

- `0` represents an empty plot.
- `1` represents a plot that already contains a flower.

Flowers cannot be planted in adjacent plots.

Given the flowerbed and an integer `n`, determine whether it is possible to plant `n` new flowers without violating the no-adjacent-flowers rule.

**LeetCode:** https://leetcode.com/problems/can-place-flowers/

---

## Approach

I solved this problem by traversing the flowerbed and checking whether each position was suitable for planting a flower.

To ensure all cases were handled correctly, I considered:

- A flowerbed containing only one plot.
- The first plot, which has only a right neighbor.
- The last plot, which has only a left neighbor.
- All middle plots, where both neighboring plots must also be empty.

Whenever a flower could be planted, I updated the flowerbed immediately and increased the count of newly planted flowers. This prevents future placements from violating the adjacency rule.

After traversing the entire flowerbed, I compared the number of planted flowers with `n` to determine the result.

---

## Algorithm

1. Initialize a counter for newly planted flowers.
2. Traverse the flowerbed.
3. Handle the single-element flowerbed separately.
4. Check the first plot.
5. Check the last plot.
6. For all remaining plots, verify that the current plot and both adjacent plots are empty.
7. If planting is possible, plant the flower, update the flowerbed, and increment the counter.
8. After traversal, return whether the counter is greater than or equal to `n`.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each plot is visited once.

- **Space Complexity:** `O(1)`
  - No additional data structures are used.

---

## Key Concepts

- Greedy Approach
- Array Traversal
- Edge Case Handling
- Simulation

---

## What I Learned

- How updating an array during traversal can simplify greedy solutions.
- The importance of handling boundary cases separately.
- How simulation can be an effective strategy for constraint-based problems.
- Why considering edge cases early helps avoid logical errors.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
