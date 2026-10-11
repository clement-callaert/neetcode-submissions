class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        array = set()
        for i in nums:
            if i in array:
                return i
            
            array.add(i)
        return None

        