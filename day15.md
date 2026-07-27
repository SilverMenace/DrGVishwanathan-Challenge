# Day 15 - Greatest Common Divisor of Strings

## Problem

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

A string `x` divides another string if the second string can be formed by concatenating one or more copies of `x`.

**LeetCode:** https://leetcode.com/problems/greatest-common-divisor-of-strings/

---

## Approach

I solved this problem in two steps.

First, I checked whether both strings could be formed using the same repeating pattern. This was done by comparing:

- `str1 + str2`
- `str2 + str1`

If these two concatenated strings are different, then no common divisor string exists, so I returned an empty string.

Otherwise, I used the **Euclidean Algorithm** to find the Greatest Common Divisor (GCD) of the lengths of both strings. The first `gcd(length(str1), length(str2))` characters of `str1` form the largest common divisor string.

---

## Algorithm

1. Compare `str1 + str2` with `str2 + str1`.
2. If they are different, return an empty string.
3. Find the GCD of the lengths of both strings using the Euclidean Algorithm.
4. Return the prefix of `str1` whose length is equal to the GCD.

---

## Complexity Analysis

- **Time Complexity:** `O(n + m)`
  - Concatenating and comparing both strings takes linear time, and the Euclidean Algorithm runs in logarithmic time with respect to the string lengths.

- **Space Complexity:** `O(1)`
  - Only a few variables are used (excluding the temporary concatenated strings).

---

## Solution (Python)

```python
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2 + str1:
            return ""

        a, b = len(str1), len(str2)

        while b > 0:
            a, b = b, a % b

        return str1[:a]
```

---

## Key Concepts

- String Manipulation
- Euclidean Algorithm
- Greatest Common Divisor (GCD)
- Pattern Matching

---

## What I Learned

- How string concatenation can be used to verify whether two strings share the same repeating pattern.
- How the Euclidean Algorithm can be applied beyond numbers to solve string-related problems.
- How the GCD of the string lengths determines the length of the largest common divisor string.
- How combining mathematical concepts with string operations can lead to elegant and efficient solutions.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
