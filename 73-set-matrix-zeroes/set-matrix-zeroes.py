class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        we need know where the zeros are present. based on this we can use 1st row as index map to say make the row/col all zero
        but if say 0th row as 0 and 2nd row as 0 so we make 0th 1st row 2nd row 0th col 0 but what happend zeros from 2nd row so we need have check 
        """
        row,col=len(matrix),len(matrix[0])
        isColZ=False
        for r in range(row):#find 0 in 0th col
            if matrix[r][0]==0:
                isColZ=True
            for c in range(1,col):
                if matrix[r][c]==0:
                    matrix[r][0]=matrix[0][c]=0 #index mapping to make later all 0
        
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0
        
        if matrix[0][0]==0:
            for c in range(col):
                matrix[0][c]=0
        
        if isColZ:
            for r in range(row):
                matrix[r][0]=0
        