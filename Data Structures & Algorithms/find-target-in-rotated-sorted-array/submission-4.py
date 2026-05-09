class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                m = left + (right - left) // 2
                
                if target < nums[m]:
                    right = m - 1
                elif target > nums[m]:
                    left = m + 1
                else:
                    return m
            return -1

        n = len(nums)
        l = 0
        r = n - 1
        
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l
        
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result
        
        return binary_search(pivot, n - 1)