# Day 20 - Valid Parentheses

## Problem

Given a string `s` containing the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine whether the input string is valid.

A string is valid if:

- Every opening bracket has a corresponding closing bracket.
- Brackets are closed in the correct order.
- Every closing bracket matches the correct opening bracket.

**LeetCode:** https://leetcode.com/problems/valid-parentheses/

---

## Approach

I solved this problem using a stack.

As I traversed the string:

- Every opening bracket was pushed onto the stack.
- For every closing bracket, I checked whether the top element of the stack was its matching opening bracket.
- If the stack was empty or the brackets didn't match, I immediately returned `False`.

After processing the entire string, the stack should be empty for the parentheses to be valid.

---

## Algorithm

1. Create an empty stack.
2. Create a dictionary that maps closing brackets to opening brackets.
3. Traverse each character in the string.
4. If it is an opening bracket, push it onto the stack.
5. Otherwise:
   - If the stack is empty, return `False`.
   - Check whether the top of the stack matches the expected opening bracket.
   - If not, return `False`.
6. Return whether the stack is empty.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Each bracket is processed exactly once.

- **Space Complexity:** `O(n)`
  - In the worst case, all opening brackets are stored in the stack.

---

## Solution (Python)

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
```

---

## Key Concepts

- Stack
- Hash Map / Dictionary
- String Traversal
- Matching Pairs

---

## What I Learned

- How a stack naturally models nested structures like parentheses.
- How a dictionary simplifies matching each closing bracket to its corresponding opening bracket.
- Why validating brackets requires checking both the type and the order of brackets.
- How early exits improve efficiency when an invalid pattern is detected.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
