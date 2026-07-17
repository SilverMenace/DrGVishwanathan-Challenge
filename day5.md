# Day 5 - Increasing Triplet Subsequence

## Problem

Given an integer array `nums`, return `true` if there exists a triplet of indices `(i, j, k)` such that:

- `i < j < k`
- `nums[i] < nums[j] < nums[k]`

Otherwise, return `false`.

**LeetCode:** https://leetcode.com/problems/increasing-triplet-subsequence/

---

## Approach

I solved this problem using a greedy approach by maintaining two variables:

- `low` stores the smallest value encountered so far.
- `mid` stores the smallest value that is greater than `low`.

While traversing the array:

- If the current number is less than or equal to `low`, update `low`.
- Otherwise, if it is less than or equal to `mid`, update `mid`.
- If the current number is greater than both `low` and `mid`, an increasing triplet has been found, so return `True`.

If the traversal completes without finding such a value, return `False`.

---

## Algorithm

1. Initialize `low` and `mid` to positive infinity.
2. Traverse each element in the array.
3. Update `low` if the current element is smaller.
4. Otherwise, update `mid` if the current element is smaller than or equal to `mid`.
5. If the current element is greater than both `low` and `mid`, return `True`.
6. If the loop ends, return `False`.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - The array is traversed only once.

- **Space Complexity:** `O(1)`
  - Only two variables are used regardless of input size.

---

## Solution (Python)

```python
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        low = mid = float('inf')

        for i in nums:
            if i <= low:
                low = i
            elif i <= mid:
                mid = i
            else:
                return True
        else:
            return False
```

---

## Key Concepts

- Greedy Algorithm
- Single Pass Traversal
- Variable Tracking
- Constant Space Optimization

---

## What I Learned

- How a greedy strategy can solve certain problems efficiently.
- How tracking only the smallest and second smallest values is enough to detect an increasing triplet.
- How to solve array problems in a single pass with constant extra space.
- The importance of updating variables in the correct order to maintain valid candidates.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
