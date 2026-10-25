# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        not_visited = [(root, 1)] 
        right = [root.val]
        while not_visited:
            node, h = not_visited.pop(-1)
            if not node:
                continue
            if len(right) < h:
                right.append(node.val)
            not_visited.append((node.left, h + 1))
            not_visited.append((node.right, h+ 1))
        return right
            
        