# Day 16 - Reverse Integer

## Problem

Given a signed 32-bit integer `x`, return the integer with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2³¹, 2³¹ - 1]`, return `0`.

**LeetCode:** https://leetcode.com/problems/reverse-integer/

---

## Approach

I solved this problem by reversing the integer using mathematical operations.

First, I determined the sign of the number and worked with its absolute value.

Then, I repeatedly:

- Extracted the last digit using the modulo operator.
- Appended it to the reversed number.
- Removed the last digit from the original number using integer division.

After all digits were processed, I restored the original sign.

Finally, I checked whether the reversed integer was within the valid 32-bit signed integer range. If it was outside the range, I returned `0`; otherwise, I returned the reversed integer.

---

## Algorithm

1. Determine the sign of the integer.
2. Convert the integer to its absolute value.
3. Initialize the reversed number as `0`.
4. While the number is not zero:
   - Extract the last digit.
   - Append it to the reversed number.
   - Remove the last digit from the original number.
5. Restore the original sign.
6. Check whether the result lies within the 32-bit signed integer range.
7. Return the reversed integer or `0` if overflow occurs.

---

## Complexity Analysis

- **Time Complexity:** `O(log₁₀ n)`
  - Each digit is processed exactly once.

- **Space Complexity:** `O(1)`
  - Only a few variables are used.

---

## Solution (Python)

```python
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
```

---

## Key Concepts

- Mathematical Operations
- Digit Extraction
- Integer Manipulation
- Overflow Handling

---

## What I Learned

- How to reverse an integer without converting it into a string.
- How modulo and integer division can be used to process digits individually.
- Why preserving the sign separately simplifies the implementation.
- The importance of checking for integer overflow when working within fixed-size integer limits.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
