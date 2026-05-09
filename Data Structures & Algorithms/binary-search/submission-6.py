class Solution:
    def binary_search(self, nums: List[int], target: int, l: int, r: int):
        if l > r:
            return -1

        m = l + (r - l) // 2

        if nums[m] > target:
            return self.binary_search(nums, target,l, m - 1 )
        elif nums[m] < target:
            return self.binary_search(nums, target,m + 1, r)
        else:
            return m

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        return self.binary_search(nums, target,l, r)

        