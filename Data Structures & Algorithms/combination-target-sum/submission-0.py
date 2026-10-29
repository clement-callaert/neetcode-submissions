class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def backtrack(i):
            total = sum(subset)
            if total == target:
                res.append(subset[:])
                return 
            if i >= len(nums) or total > target:
                return
            
            subset.append(nums[i])
            backtrack(i)
            subset.pop()
            backtrack(i+ 1)

        backtrack(0)
        return res
            