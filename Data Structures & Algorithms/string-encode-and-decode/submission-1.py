class Solution:

    def encode(self, strs: List[str]) -> str:
        string_encoded = ""
        for string in strs:
            string_encoded += string + "Ÿ"
        return string_encoded

    def decode(self, s: str) -> List[str]:
        list_decode = []
        string_sum = ""
        for string in s:
            if string == "Ÿ":
                list_decode.append(string_sum)
                string_sum = ""
            else:
                string_sum += string
        return list_decode

