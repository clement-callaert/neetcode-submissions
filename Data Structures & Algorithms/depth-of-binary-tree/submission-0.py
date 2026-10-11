# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        hashmap = {root: 0}
        maxdepth = 0
        not_visited = [root]
        while not_visited:
            node = not_visited.pop()
            if node.left:
                not_visited.append(node.left)
            if node.right:
                not_visited.append(node.right)
            hashmap[node.left] = hashmap[node] + 1
            hashmap[node.right] = hashmap[node] + 1
            if hashmap[node] + 1 > maxdepth:
                maxdepth = hashmap[node] + 1
        return maxdepth