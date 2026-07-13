# Day 1 - Two Sum

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

**LeetCode:** https://leetcode.com/problems/two-sum/

---

## Approach

For this solution, I used the **Brute Force** approach.

I iterate through every element in the array using the first loop. For each element, I check every remaining element using a second loop to see if their sum equals the target.

If the required pair is found, I immediately return their indices. Since every possible pair is checked, this approach always finds the correct answer.

---

## Algorithm

1. Traverse the array using index `i`.
2. For every `i`, traverse the remaining elements using index `j`.
3. Check if `nums[i] + nums[j] == target`.
4. If true, return `{i, j}`.
5. If no valid pair is found, return `{-1}`.

---

## Complexity Analysis

- **Time Complexity:** `O(n²)`
  - Every possible pair of elements is checked in the worst case.

- **Space Complexity:** `O(1)`
  - No additional data structures are used.

---

## Solution (C++)

```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); i++) {
            for(int j = i + 1; j < nums.size(); j++) {
                if(nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {-1};
    }
};
```

---

## Key Concepts

- Arrays
- Nested Loops
- Brute Force
- Pair Comparison

---

## What I Learned

- How to solve a problem using a straightforward brute-force approach.
- How nested loops can be used to compare every possible pair.
- The importance of analyzing time and space complexity.
- Brute-force solutions provide a strong foundation before learning optimized approaches like Hash Maps.

---

⭐ This solution is part of my **#100DaysOfCode** and **#DRGVishvanathanChallenge** journey.
