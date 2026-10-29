class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        subset = []
        def backtrack(i, total):
            if total == target:
                res.add(tuple(subset))
                return 
            if i >= len(candidates) or total > target:
                return
            subset.append(candidates[i])
            backtrack(i + 1, total + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1    
            backtrack(i + 1, total)
        backtrack(0, 0)
        return [list(combination) for combination in res]