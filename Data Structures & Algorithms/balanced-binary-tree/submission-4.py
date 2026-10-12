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
            if node.left and node.right:
                lenght_left = RecMaxLenght(node.left)
                lenght_right = RecMaxLenght(node.right)
                if abs(lenght_left - lenght_right) > 1:
                    return False
                not_visited.append(node.left)
                not_visited.append(node.right)
            elif node.left:
                lenght_left = RecMaxLenght(node.left)
                if lenght_left > 1:
                    return False
                not_visited.append(node.left)
            elif node.right:
                lenght_right = RecMaxLenght(node.right)
                if lenght_right > 1:
                    return False
                not_visited.append(node.right)

        return True





        