class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i, string in enumerate(strs):
            hashmap[str(sorted(list(string)))].append(string)
        
        return list(hashmap.values())
        