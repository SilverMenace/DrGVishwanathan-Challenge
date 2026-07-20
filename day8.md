# Day 8 - Reverse Vowels of a String

## Problem

Given a string `s`, reverse only the vowels in the string and return the resulting string.

The vowels are:

- `a`, `e`, `i`, `o`, `u`
- `A`, `E`, `I`, `O`, `U`

**LeetCode:** https://leetcode.com/problems/reverse-vowels-of-a-string/

---

## Approach

I solved this problem by separating the vowels from the original string.

First, I converted the string into a list of characters so that individual characters could be modified.

Then I:

- Extracted every vowel into a separate list.
- Reversed that list of vowels.
- Traversed the original character list again.
- Whenever a vowel was encountered, I replaced it with the next vowel from the reversed list.
- Finally, I joined the characters back into a string.

This ensures that only the vowels change position while every consonant remains in its original place.

---

## Algorithm

1. Convert the string into a list of characters.
2. Store all vowels in a separate list.
3. Reverse the vowel list.
4. Traverse the original character list.
5. Whenever a vowel is found, replace it with the next reversed vowel.
6. Join the character list into a string and return it.

---

## Complexity Analysis

- **Time Complexity:** `O(n)`
  - The string is traversed a constant number of times.

- **Space Complexity:** `O(n)`
  - An additional list is used to store the vowels.

---

## Solution (Python)

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        orig = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        mod = [x for x in orig if x in vowels]
        mod1 = mod[::-1]

        j = 0

        for i in range(len(orig)):
            if orig[i] in vowels:
                orig[i] = mod1[j]
                j += 1

        return ''.join(orig)
```

---

## Key Concepts

- String Manipulation
- Lists
- List Comprehension
- Character Traversal
- Selective Replacement

---

## What I Learned

- How converting a string into a list allows characters to be modified easily.
- How list comprehensions can be used to extract specific characters efficiently.
- How reversing only selected elements can simplify string manipulation problems.
- How combining traversal with selective replacement leads to a clean and readable solution.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
