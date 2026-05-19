class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        max_len = 0
        for char in s:
            
            while char in substring:
                substring.pop(0)
                
            substring.append(char)
            if max_len < len(substring):
                max_len = len(substring)

        return max_len  