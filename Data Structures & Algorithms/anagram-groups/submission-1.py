class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i, string in enumerate(strs):
            sort = str(sorted(list(string)))
            if sort not in hashmap:
                hashmap[sort] = [string]
            else:
                hashmap[sort].append(string)
        
        return list(hashmap.values())
        