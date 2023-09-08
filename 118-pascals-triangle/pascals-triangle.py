class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        #sliding window
        res=[[1],[1,1]]

        for i in range(2,numRows):
            newRow=[1] #add inital 1 in new row
            l=0
            prevRow=res[-1]
            for r in range(1,len(prevRow)):
                newRow.append(prevRow[l]+prevRow[r])
                l+=1
            
            newRow.append(1) #add 1 at last
            res.append(newRow)
        
        return res

        