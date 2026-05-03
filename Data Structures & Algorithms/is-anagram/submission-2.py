class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(list(s)) != len(list(t)):
            return False

        hashmap = defaultdict(int)
        for i,_ in enumerate(s):
            hashmap[s[i]] += 1
            hashmap[t[i]] -= 1
        for i in hashmap.values():
            if i != 0:
                return False
        return True