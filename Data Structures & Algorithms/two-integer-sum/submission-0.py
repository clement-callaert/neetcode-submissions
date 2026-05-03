class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i, num in enumerate(nums):
            diff = - num + target
            
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[diff] = i
        return None


        