class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i, num in enumerate(nums):
            hashmap[num] += 1
        results = sorted(hashmap.keys(), key=hashmap.get, reverse=True)
        return results[:k]
        