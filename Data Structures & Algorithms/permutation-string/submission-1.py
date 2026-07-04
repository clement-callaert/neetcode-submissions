class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charset = set(s1)
        compteur = {}
        for char in s1:
            compteur[char] = compteur.get(char, 0) + 1
        if len(s2) < len(s1):
            return False
        for i in range(0, len(s2)):
            r = 0
            hashmap = dict.fromkeys(charset, 0)
            while r <= len(s1) and i + r < len(s2):
                if s2[i + r] not in charset or hashmap[s2[i + r]] >= compteur[s2[i + r]]:
                    break
                hashmap[s2[i + r]] += 1
                if r == len(s1) - 1:
                    return True
                r += 1
        return False
                
            