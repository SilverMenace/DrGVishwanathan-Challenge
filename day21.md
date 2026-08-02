# Day 21 - 4Sum

## Problem

Given an integer array `nums` and an integer `target`, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- All indices are distinct.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

The solution set must not contain duplicate quadruplets.

**LeetCode:** https://leetcode.com/problems/4sum/

---

## Approach

I solved this problem by combining sorting with the two-pointer technique.

First, I sorted the array so that duplicate values could be handled easily.

Then:

- Fixed the first number using the first loop.
- Fixed the second number using the second loop.
- Used two pointers (`left` and `right`) to search for the remaining two numbers.
- Compared the sum of all four numbers with the target.
- If a valid quadruplet was found, I stored it and skipped duplicate values.
- Otherwise, I moved the pointers depending on whether the current sum was smaller or larger than the target.

This approach efficiently avoids duplicate quadruplets while checking all possible combinations.

---

## Algorithm

1. Sort the array.
2. Iterate through the array to fix the first number.
3. Iterate again to fix the second number.
4. Initialize two pointers:
   - `left = j + 1`
   - `right = n - 1`
5. Compute the sum of the four numbers.
6. If the sum equals the target:
   - Store the quadruplet.
   - Skip duplicate values.
7. If the sum is smaller than the target, move the left pointer.
8. Otherwise, move the right pointer.
9. Continue until all valid quadruplets are found.

---

## Complexity Analysis

- **Time Complexity:** `O(n³)`
  - Two nested loops combined with a two-pointer search.

- **Space Complexity:** `O(1)`
  - Excluding the output list.

---

## Solution (Python)

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans
```

---

## Key Concepts

- Sorting
- Two Pointers
- Nested Loops
- Duplicate Handling

---

## What I Learned

- How the two-pointer technique can be extended beyond 2Sum and 3Sum problems.
- Why sorting simplifies both searching and duplicate elimination.
- How skipping repeated values ensures only unique quadruplets are returned.
- How combining nested loops with two pointers significantly reduces unnecessary comparisons compared to a brute-force approach.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
