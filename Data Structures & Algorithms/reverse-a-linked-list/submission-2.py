# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listnode = None
        while head != None:
            listnode = ListNode(head.val, next=listnode)
            head = head.next
        return listnode

        