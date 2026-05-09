class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            
            if nums[l] > nums[r]:
                if nums[l] < target:
                    l += 1
                elif nums[r] > target:
                    r -= 1
                elif nums[l] == target:
                    return l
                elif nums[r] == target:
                    return r
                else:
                    return -1
            else:
                if nums[l] < target:
                    l += 1
                elif nums[l] > target:
                    return -1
                else:
                    return l
        return -1