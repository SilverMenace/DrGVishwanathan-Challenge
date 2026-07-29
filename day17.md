# Day 17 - Integer to Roman

## Problem

Given an integer `num`, convert it to its corresponding Roman numeral.

Roman numerals are represented using the symbols:

- I = 1
- V = 5
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

Special combinations such as `IV`, `IX`, `XL`, `XC`, `CD`, and `CM` are also used.

**LeetCode:** https://leetcode.com/problems/integer-to-roman/

---

## Approach

I solved this problem using a Greedy Approach.

I maintained two lists:

- One containing the integer values in descending order.
- Another containing the corresponding Roman numeral symbols.

Starting from the largest value, I repeatedly checked whether it could be subtracted from the given number.

If it could:

- Append the corresponding Roman symbol to the result.
- Subtract the value from the number.
- Continue until the value could no longer be used.

This process is repeated for every value until the number becomes zero.

---

## Algorithm

1. Create two arrays:
   - Integer values in descending order.
   - Corresponding Roman numeral symbols.
2. Initialize an empty result string.
3. Traverse the arrays from beginning to end.
4. While the current value is less than or equal to the number:
   - Append the corresponding Roman symbol.
   - Subtract the value from the number.
5. Return the final Roman numeral string.

---

## Complexity Analysis

- **Time Complexity:** `O(1)`
  - The number of Roman numeral values is fixed, so the algorithm performs a constant amount of work.

- **Space Complexity:** `O(1)`
  - Apart from the output string, only a fixed number of variables are used.

---

## Solution (Python)

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        values = [1000, 900, 500, 400, 100, 90, 50, 40,
                  10, 9, 5, 4, 1]

        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        result = ""

        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]

        return result
```

---

## Key Concepts

- Greedy Algorithm
- Arrays / Lists
- String Construction
- Number Manipulation

---

## What I Learned

- How a greedy strategy can simplify conversion problems.
- Why storing values and symbols in parallel arrays makes the implementation clean and readable.
- How repeatedly choosing the largest valid Roman numeral guarantees the correct result.
- How predefined mappings can eliminate the need for complex conditional logic.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
