# Day 18 - Roman to Integer

## Problem

Given a Roman numeral, convert it into its corresponding integer.

Roman numerals follow both additive and subtractive rules. For example:

- III = 3
- IV = 4
- IX = 9
- LVIII = 58
- MCMXCIV = 1994

**LeetCode:** https://leetcode.com/problems/roman-to-integer/

---

## Approach

I solved this problem using a Hash Map to store the value of each Roman numeral.

I traversed the string from left to right.

For every character:

- If its value was smaller than the value of the next character, I subtracted it from the answer.
- Otherwise, I added its value.

This correctly handles both the normal addition cases and the special subtractive cases like `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`.

---

## Algorithm

1. Store all Roman numeral values in a dictionary.
2. Initialize the answer as `0`.
3. Traverse the string from left to right.
4. Compare the current numeral with the next one.
5. If the current value is smaller, subtract it.
6. Otherwise, add it.
7. Return the final integer value.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each Roman numeral is processed exactly once.

- **Space Complexity:** `O(1)`
  - The dictionary contains a fixed number of Roman numeral mappings.

---

## Solution (Python)

```python
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
```

---

## Key Concepts

- Hash Map / Dictionary
- String Traversal
- Conditional Logic
- Simulation

---

## What I Learned

- How a dictionary provides constant-time lookup for Roman numeral values.
- How subtractive notation can be handled by comparing adjacent characters.
- How a single traversal is enough to solve the problem efficiently.
- How understanding the rules of Roman numerals simplifies the implementation.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
