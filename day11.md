# Day 11 - Container With Most Water

## Problem

Given an integer array `height`, where each element represents the height of a vertical line, find two lines that together with the x-axis form a container capable of holding the maximum amount of water.

Return the maximum amount of water the container can store.

**LeetCode:** https://leetcode.com/problems/container-with-most-water/

---

## Approach

I solved this problem using the Two Pointers technique.

One pointer starts at the beginning of the array, while the other starts at the end. At each step:

- Calculate the width between the two pointers.
- Compute the area using the shorter of the two heights.
- Update the maximum area found so far.
- Move the pointer pointing to the shorter height inward.

The reasoning is that the shorter line limits the container's height. Moving the taller line cannot increase the area unless the shorter line also changes.

The process continues until the two pointers meet.

---

## Algorithm

1. Initialize two pointers:
   - `left = 0`
   - `right = len(height) - 1`
2. Initialize `max_area = 0`.
3. While `left < right`:
   - Calculate the width.
   - Calculate the current area.
   - Update the maximum area.
   - Move the pointer with the smaller height inward.
4. Return the maximum area.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each pointer moves at most once across the array.

- **Space Complexity:** `O(1)`
  - Only a few variables are used.

---

## Solution (Python)

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

## Key Concepts

- Two Pointers
- Greedy Observation
- Array Traversal
- Area Calculation

---

## What I Learned

- How the two-pointer technique reduces the search space efficiently.
- Why the shorter line determines the current container's capacity.
- How moving the pointer at the shorter height helps explore better solutions.
- How greedy observations can transform a brute-force solution into a linear-time algorithm.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
