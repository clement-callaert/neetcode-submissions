class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        top = 0
        bott = height - 1
        l = 0
        r = width - 1

        while top <= bott:
            
            m1 = top + (bott - top) // 2
            if matrix[m1][r] < target:
                top = m1 + 1
            elif matrix[m1][l] > target:
                bott = m1 - 1
            else:
                nums = matrix[m1]
                while l <= r:
                    m2 =  l + (r - l) // 2

                    if nums[m2] > target:
                        r = m2 - 1
                    elif nums[m2] < target:
                        l = m2 + 1
                    else:
                        return True
        return False