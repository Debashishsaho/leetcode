# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        li=[]
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        current=head
        partsize=count//k
        reminder=count%k
        for i in range(k):
            part_head=current
            part_len=partsize + (1 if i<reminder else 0)

            for _ in range(part_len-1):
                if current:
                    current=current.next
            
            if current:
                next_part=current.next
                current.next=None
                current=next_part
            li.append(part_head)
        return li