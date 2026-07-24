# Day 12 - Longest Palindromic Substring

## Problem

Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same forward and backward.

**LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/

---

## Approach

I solved this problem using the **Expand Around Center** technique.

Every palindrome has a center. For each character in the string, I checked two cases:

- The current character as the center (odd-length palindrome).
- The gap between the current and next character as the center (even-length palindrome).

For both cases, I expanded outward as long as the characters on both sides were equal.

Whenever a longer palindrome was found, I updated the starting and ending indices.

Finally, I returned the substring between those indices.

---

## Algorithm

1. Handle the empty string case.
2. Initialize variables to store the start and end indices of the longest palindrome.
3. Define a helper function to expand around a given center.
4. Traverse each character in the string.
5. Expand for both odd-length and even-length palindromes.
6. Update the longest palindrome whenever a longer one is found.
7. Return the substring from `start` to `end`.

---

## Complexity Analysis

- **Time Complexity:** `O(n²)`
  - Each center may expand across the string in the worst case.

- **Space Complexity:** `O(1)`
  - Only a few extra variables are used.

---

## Solution (Python)

```python
class Solution(object):
    def longestPalindrome(self, s):

        if not s:
            return ""

        start = end = 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):

            l1, r1 = expand(i, i)

            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
```

---

## Key Concepts

- Expand Around Center
- Two Pointers
- String Traversal
- Palindrome Detection

---

## What I Learned

- How every palindrome can be expanded from its center.
- Why both odd-length and even-length palindromes must be checked.
- How maintaining the start and end indices avoids creating unnecessary substrings.
- How expanding around each center provides a clean and efficient solution for palindrome problems.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
