class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        list_sum = []
        n = len(nums)
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if i != 0 and nums[i - 1] == num:
                continue
            
            l, r = i + 1, n - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]

                if three_sum == 0:
                    list_sum.append([num , nums[l] , nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
        return list_sum
                
        