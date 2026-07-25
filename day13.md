# Day 13 - Add Two Numbers

## Problem

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain leading zeros, except for the number `0` itself.

**LeetCode:** https://leetcode.com/problems/add-two-numbers/

---

## Approach

I solved this problem by traversing both linked lists simultaneously while maintaining a carry value.

To simplify the construction of the result linked list, I created a dummy node. During each iteration:

- Read the current value from each linked list (or `0` if a list has ended).
- Add both values along with the carry.
- Create a new node containing the last digit of the sum.
- Update the carry for the next iteration.
- Move to the next nodes in both linked lists.

The loop continues until both linked lists have been completely traversed and there is no remaining carry.

Finally, I returned the linked list starting from the node after the dummy node.

---

## Algorithm

1. Create a dummy node and set a pointer to it.
2. Initialize the carry as `0`.
3. Traverse both linked lists while either list still has nodes or the carry is non-zero.
4. Read the current values from both lists.
5. Compute the sum of both values and the carry.
6. Create a new node containing `sum % 10`.
7. Update the carry using `sum // 10`.
8. Move to the next nodes in the linked lists.
9. Return the linked list starting after the dummy node.

---

## Complexity Analysis

- **Time Complexity:** `O(max(m, n))`
  - Each node from both linked lists is processed once.

- **Space Complexity:** `O(max(m, n))`
  - A new linked list is created to store the result.

---

## Solution (Python)

```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
```

---

## Key Concepts

- Linked Lists
- Dummy Node
- Carry Handling
- Iterative Traversal

---

## What I Learned

- How a dummy node simplifies linked list construction.
- How to process two linked lists of different lengths simultaneously.
- How carrying the overflow digit mirrors the way addition is performed manually.
- How iterative traversal makes linked list problems clean and efficient.

---

⭐ This solution is part of my **#21DaysOfCode** and **#DRGVishvanathanChallenge** journey.
