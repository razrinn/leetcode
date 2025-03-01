# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        root = list1 if list1.val <= list2.val else list2
        curr = root
        n1 = list1.next if root == list1 else list1
        n2 = list2.next if root == list2 else list2

        while n1 and n2:
            if n1.val <= n2.val:
                curr.next = n1
                n1 = n1.next
            else:
                curr.next = n2
                n2 = n2.next
            curr = curr.next

        curr.next = n1 or n2

        return root