# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            left = p
            right = q
        else:
            left = q
            right = p
        ancestor = root
        not_visited = [root]
        while not_visited:
            node = not_visited.pop()
            if not node:
                continue
            if node.val == q.val or node.val == p.val:
                
                not_visited.append(node.right)
                not_visited.append(node.left)

            if node.val > right.val:
                not_visited.append(node.left)
                ancestor = node
            elif node.val < left.val:
                not_visited.append(node.right)
                ancestor = node
            else:
                return node
        return ancestor


            

            