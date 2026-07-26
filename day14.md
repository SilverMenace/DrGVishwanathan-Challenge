# Day 14 - Zigzag Conversion

## Problem

Given a string `s` and an integer `numRows`, arrange the characters in a zigzag pattern across the specified number of rows and then read the rows one by one to produce the converted string.

**LeetCode:** https://leetcode.com/problems/zigzag-conversion/

---

## Approach

I solved this problem by simulating the zigzag traversal.

First, I handled the edge cases where the zigzag pattern would remain unchanged, such as when there is only one row or when the number of rows is greater than or equal to the string length.

Next, I created a list of strings, where each element represented one row of the zigzag pattern.

While traversing the input string:

- Add the current character to the current row.
- Change the traversal direction whenever the first or last row is reached.
- Move to the next row according to the current direction.

After processing all characters, I concatenated every row to produce the final converted string.

---

## Algorithm

1. Handle the edge cases.
2. Create a list containing one empty string for each row.
3. Initialize the current row and traversal direction.
4. Traverse each character in the input string.
5. Append the character to the current row.
6. Reverse the traversal direction whenever the first or last row is reached.
7. Move to the next appropriate row.
8. Join all rows together and return the final string.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Every character is processed exactly once.

- **Space Complexity:** `O(n)`
  - The rows collectively store all characters of the input string.

---

## Solution (Python)

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            if going_down:
                current_row += 1
            else:
                current_row -= 1

        return "".join(rows)
```

---

## Key Concepts

- Simulation
- String Manipulation
- Direction Tracking
- Arrays / Lists

---

## What I Learned

- How simulating a process can simplify problems involving patterns.
- How direction tracking helps navigate between rows efficiently.
- How storing intermediate results row-wise makes reconstruction straightforward.
- How handling edge cases early keeps the main logic clean and concise.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
