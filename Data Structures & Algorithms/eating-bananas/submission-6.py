class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_pile = max(piles)
        stack = [max_pile]

        l = 1
        r = max_pile - 1
        while l <= r:
            m = l + (r - l) // 2
            time = 0
            for pile in piles:
                x = pile / m
                time += max(int(x) + (1 if x > int(x) else 0), 1)

            if time > h:
                l = m + 1
            elif time <= h:
                r = m - 1
                stack.append(m)

        return stack[-1]

                

