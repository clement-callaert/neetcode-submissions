class Solution:
    def maxArea(self, heights: List[int]) -> int:
        hashmap = {}
        n = len(heights)
        l = 0
        r = n - 1
        v_max = 0
        while l < r:
            v = min(heights[l], heights[r]) * (r - l)

            if v > v_max:
                v_max = v

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return int(v_max)

