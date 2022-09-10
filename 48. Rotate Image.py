class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n - i -1, i - 1, -1):
                matrix[i][j], matrix[j][n - i - 1] = matrix[j][n - i - 1], matrix[i][j]

            for j in range(i, n - i):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
                
            matrix[i][n - i - 1], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][n - i - 1]
            
            for j in range(i, n - i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
            matrix[i][n - i - 1], matrix[n - i - 1][n - i - 1] = matrix[n - i - 1][n - i - 1], matrix[i][n - i - 1]
            
            p1 = i + 1
            p2 = n - i - 2
            while p1 < p2:
                matrix[i][p1], matrix[i][p2] = matrix[i][p2], matrix[i][p1]
                matrix[n - i - 1][p1], matrix[n - i - 1][p2] = matrix[n - i - 1][p2], matrix[n - i - 1][p1]
                p1 += 1
                p2 -= 1