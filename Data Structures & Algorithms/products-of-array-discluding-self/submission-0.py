class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        list_product = []
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(num)
                suffix.append(nums[::-1][i])
            else : 
                prefix.append(num * prefix[-1]) 
                suffix.append(nums[::-1][i] * suffix[-1])

        for i, num in enumerate(nums):
            list_product.append(prefix[i] * suffix[::-1][i + 1])

        return list_product
        