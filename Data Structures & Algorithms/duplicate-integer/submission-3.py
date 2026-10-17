class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)
        a = float("inf")
        for x in nums_sorted:
            if x == a:
                return True
            a = x
        return False