class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c=[[*map(all,q)] for q in (matrix,zip(*matrix))]
        for i,j in product(range(len(matrix)),range(len(matrix[0]))):
            matrix[i][j]*=r[i]&c[j]
        