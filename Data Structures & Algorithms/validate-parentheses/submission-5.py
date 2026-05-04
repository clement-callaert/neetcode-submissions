class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { '{':'}', '(':')', '[':']'}
        stack = []
        for char in s:
            if char in hashmap:
                stack.append(hashmap[char])
            elif char not in hashmap:
                if not stack or stack[-1] != char:
                    return False
                else:
                    stack.pop(-1)
        return True if not stack else False
                
            

        