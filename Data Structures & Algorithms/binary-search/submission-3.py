class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        if nums[0] == target:
            return 0
        while l < r:
            
            if nums[l] < target:
                l += 1
            if nums[r] > target:
                r -= 1
            if nums[l] == target:
                return l

        return -1

        