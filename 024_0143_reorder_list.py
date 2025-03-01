from typing import Optional
# watch solution, need revisit
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # find middle
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second part
        second_part = slow.next
        prev, slow.next = None, None
        while second_part:
            tmp = second_part.next
            second_part.next = prev
            prev = second_part
            second_part = tmp

        # merge list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2