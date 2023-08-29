class Solution:
    def bestClosingTime(self, customers: str) -> int:
        #prefix N and postfix Y
        n=len(customers)
        prefix_N=[0]*(n+1)
        postfix_Y=[0]*(n+1)

        for i in range(1,n+1):
            prefix_N[i]=prefix_N[i-1]
            if customers[i-1]=="N":
                prefix_N[i]+=1

        for i in range(n-1,-1,-1):
            postfix_Y[i]=postfix_Y[i+1]
            if customers[i]=="Y":
                postfix_Y[i]+=1
        
        min_pen,idx=float('inf'),0
        for i in range(n+1):
            pen=prefix_N[i]+postfix_Y[i]
            if pen<min_pen:
                min_pen=pen
                idx=i
        
        return idx