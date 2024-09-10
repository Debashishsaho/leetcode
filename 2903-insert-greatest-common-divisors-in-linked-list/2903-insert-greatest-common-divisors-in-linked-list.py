# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current=head.next
        prev=head
        while current:
            common_div=math.gcd(current.val,prev.val)
            new_node=ListNode(common_div)
            new_node.next=current
            prev.next=new_node
            prev=current
            current=current.next
        return head