from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    # use set. slightly faster, but need more memory
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        hmap = set()
        while head:
            if head in hmap:
                return True
            hmap.add(head)
            head = head.next
        return False