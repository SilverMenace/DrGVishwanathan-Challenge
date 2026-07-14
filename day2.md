# Day 2 - Reverse Words in a String

## Problem

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The returned string should contain the words in reverse order separated by a single space, without any leading, trailing, or extra spaces.

**LeetCode:** https://leetcode.com/problems/reverse-words-in-a-string/

---

## Approach

For this solution, I used Python's built-in string functions along with reverse traversal.

First, I split the input string into a list of words using `split()`. This automatically removes any leading, trailing, or extra spaces between words.

Then, I traversed the list from the last element to the first, storing each word in a new list. Finally, I joined the reversed words into a single string using `" ".join()`.

This approach is simple, readable, and correctly handles all the spacing conditions mentioned in the problem.

---

## Algorithm

1. Split the input string into a list of words using `split()`.
2. Create an empty list to store the reversed words.
3. Traverse the list from the last index to the first.
4. Append each word to the new list.
5. Join the words using `" ".join()` and return the resulting string.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - Splitting the string, traversing the list, and joining the words each take linear time.

- **Space Complexity:** `O(n)`
  - An additional list is used to store the reversed words.

---

## Solution (Python)

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = s.split()
        list1 = []

        for i in range(len(l) - 1, -1, -1):
            list1.append(l[i])

        x = ' '.join(list1)
        return x
```

---

## Key Concepts

- String Manipulation
- String Splitting (`split()`)
- Reverse Traversal
- List Operations
- String Joining (`join()`)

---

## What I Learned

- How `split()` automatically removes unnecessary spaces from a string.
- How to traverse a list in reverse using indices.
- How `join()` can efficiently construct a string from a list of words.
- How combining built-in functions with basic list operations leads to clean and readable solutions.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
