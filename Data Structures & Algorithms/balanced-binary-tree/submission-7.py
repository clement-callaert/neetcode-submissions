# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def RecMaxLenght(node):
            if not node:
                return 0

            return 1 + max(RecMaxLenght(node.left), RecMaxLenght(node.right))

        not_visited = [root]
        while not_visited:
            node = not_visited.pop()
            if abs(RecMaxLenght(node.right) - RecMaxLenght(node.left)) > 1:
                return False
            if node.left: not_visited.append(node.left)
            if node.right: not_visited.append(node.right)

        return True





        