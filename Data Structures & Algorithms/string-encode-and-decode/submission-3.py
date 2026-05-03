class Solution:

    def encode(self, strs: List[str]) -> str:
        string_encoded = ""
        for string in strs:
            string_encoded += string + "Ÿ"
        return string_encoded

    def decode(self, s: str) -> List[str]:
        list_decode = s.strip().split("Ÿ")
        list_decode.pop()
        
        return list_decode

