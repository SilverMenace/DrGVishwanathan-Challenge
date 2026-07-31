# Day 19 - Longest Common Prefix

## Problem

Given an array of strings `strs`, return the longest common prefix among all the strings.

If there is no common prefix, return an empty string.

**LeetCode:** https://leetcode.com/problems/longest-common-prefix/

---

## Approach

I solved this problem by treating the first string as the initial common prefix.

Then, I compared this prefix with every other string in the array.

If a string did not start with the current prefix, I repeatedly removed the last character from the prefix until either:

- The string started with the prefix, or
- The prefix became empty.

After checking all the strings, the remaining prefix was the longest common prefix.

---

## Algorithm

1. If the array is empty, return an empty string.
2. Initialize the first string as the current prefix.
3. Traverse every remaining string.
4. While the current string does not start with the prefix:
   - Remove the last character from the prefix.
   - If the prefix becomes empty, return an empty string.
5. Return the final prefix.

---

## Complexity Analysis

- **Time Complexity:** `O(n × m)`
  - Each string may be compared multiple times while shortening the prefix.

- **Space Complexity:** `O(1)`
  - Only the prefix variable is used.

---

## Solution (Python)

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix
```

---

## Key Concepts

- String Manipulation
- Prefix Matching
- Iterative Comparison
- Arrays / Lists

---

## What I Learned

- How using the first string as the initial prefix simplifies the solution.
- How repeatedly shortening the prefix efficiently finds the common portion shared by all strings.
- How built-in string methods like `startswith()` make prefix comparison straightforward.
- The importance of handling edge cases such as an empty input array or no common prefix.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
