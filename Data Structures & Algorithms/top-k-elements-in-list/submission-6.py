class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        array = [[] for _ in range(n+1)]

        for num, count in hashmap.items():
            array[count].append(num)
        result = []
        for x in array[::-1]:
            if x:
                for num in x:
                    result.append(num)
        return result[:k]
        