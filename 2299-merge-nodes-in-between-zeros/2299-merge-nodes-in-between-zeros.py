# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        while head:
            sume=0
            while head and head.val!=0:
                sume +=head.val
                head=head.next
            if head:
                head=head.next
            if sume>0:
                current.next=ListNode(sume)
                current=current.next 
        return dummy.next