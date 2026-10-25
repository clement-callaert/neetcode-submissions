# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        not_visited = [(root,0)]
        hashmap = defaultdict(list)
        while not_visited:
            node, h = not_visited.pop(0)
            if node:
                not_visited.append((node.left, h + 1))
                not_visited.append((node.right, h + 1))
                hashmap[h].append(node.val)

        return list(hashmap.values())

        