from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        print(matrix)
        for i in range(n):
            matrix[i] = list(reversed(matrix[i]))
        return matrix

obj = Solution()
print(obj.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))