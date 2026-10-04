# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
            
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                q = queue.popleft()
                level.append(q.val)
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)
            
            res.append(level)
        
        return res