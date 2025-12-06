class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        so how reverse the each row and swap the col value in place
        look at output last row is 1st value is at top
        """
        n=len(matrix)
        matrix.reverse()
        #now tranpose each diagonal
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        