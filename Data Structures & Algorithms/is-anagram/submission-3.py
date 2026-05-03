class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(list(s)) == sorted(list(t)) else False