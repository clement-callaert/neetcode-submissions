class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        sum_water = 0
        prefix = []
        suffix = []
        max_pref = 0
        max_suffix = 0

        for i, num in enumerate(height):
            
            if num > max_pref:
                max_pref = num
            prefix.append(max_pref)

        for i, num in enumerate(height[::-1]):
            
            if num > max_suffix:
                max_suffix = num
            suffix.append(max_suffix)

        suffix = suffix[::-1]

        for i, num in enumerate(height):

            sum_water += min(suffix[i], prefix[i]) - num

        return sum_water
            