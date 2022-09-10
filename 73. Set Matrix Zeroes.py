class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        t = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: t.add((i,j))
                    
        for item in t:
            row , col = item
            for i in range(n):
                matrix[row][i] = 0
            for i in range(m):
                matrix[i][col] = 0