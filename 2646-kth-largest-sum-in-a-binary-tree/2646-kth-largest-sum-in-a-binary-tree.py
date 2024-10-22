# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum=[]
        queue=deque([root])
        while queue:
            current_sum=0
            for _ in range(len(queue)):
                node = queue.popleft()
                current_sum +=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level_sum.append(current_sum)
        if len(level_sum)<k:
            return -1
        return heapq.nlargest(k,level_sum)[-1]