class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        min_arr = nums[0]
        while l <= r:
            

            if nums[l] > nums[r]:
                min_arr = nums[r]
                r -= 1
                
            else:
                return nums[l] if nums[l] < min_arr else min_arr

        




        