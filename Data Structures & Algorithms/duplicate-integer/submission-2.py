class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        L = []
        for i, num in enumerate(nums):
            if num in L:
                return True
            L.append(num)
            

        return False
        