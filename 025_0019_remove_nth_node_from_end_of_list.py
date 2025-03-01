from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lead, lag = head, head
        for i in range(n):
            lead = lead.next

        while lead and lead.next:
            lead = lead.next
            lag = lag.next
        if lag == head and lead == None:
            head = head.next
        else:
            lag.next = lag.next.next if lag.next else None
        return head

    # slightly different solution. use dummy node
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lead, lag = dummy, dummy
        for _ in range(n + 1):
            lead = lead.next

        while lead:
            lead = lead.next
            lag = lag.next

        lag.next = lag.next.next if lag.next else None
        return dummy.next