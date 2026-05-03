class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, num in enumerate(numbers):
            delta = target - num

            if num in hashmap:
                return [hashmap[num] + 1, i + 1]

            hashmap[delta] = i

        return None

        