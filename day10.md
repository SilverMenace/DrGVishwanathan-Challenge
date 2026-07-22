# Day 10 - Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the longest substring without repeating characters.

**LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

## Approach

I solved this problem using the Sliding Window technique along with a set.

The window is represented by two pointers:

- `left` marks the beginning of the current substring.
- `right` expands the substring one character at a time.

As I traversed the string:

- If the current character was not already present in the set, I added it to the window.
- If a duplicate character was found, I repeatedly removed characters from the left side of the window until the duplicate was eliminated.
- After every iteration, I updated the maximum length of a valid substring found so far.

This approach ensures that the current window always contains unique characters.

---

## Algorithm

1. Initialize an empty set.
2. Initialize `left = 0` and `longest = 0`.
3. Traverse the string using the `right` pointer.
4. While the current character already exists in the set:
   - Remove the leftmost character from the set.
   - Move the `left` pointer forward.
5. Add the current character to the set.
6. Update the maximum substring length.
7. Return the maximum length.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each character is added to and removed from the set at most once.

- **Space Complexity:** `O(min(n, m))`
  - The set stores only the characters in the current window, where `m` is the size of the character set.

---

## Key Concepts

- Sliding Window
- Hash Set
- Two Pointers
- String Traversal

---

## What I Learned

- How the sliding window technique efficiently solves substring problems.
- How a set provides constant-time lookup for detecting duplicate characters.
- How dynamically adjusting the window avoids unnecessary repeated work.
- How combining two pointers with a hash set leads to an optimal linear-time solution.

---

## Solution (Python)

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
```

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
