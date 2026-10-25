# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        not_visited = [(root, root.val)]
        number_good = 0
        while not_visited:
            node, x = not_visited.pop(-1)
            if not node:
                continue
            if x <= node.val:
                number_good += 1
                not_visited.append((node.left, node.val))
                not_visited.append((node.right, node.val))
            else:
                not_visited.append((node.left, x))
                not_visited.append((node.right, x))
        return number_good
