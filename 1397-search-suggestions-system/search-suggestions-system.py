class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        sort and every search we need to show max of 3 
        2 ptr get the valid window and from here give max of 3
        find the window then append to res
        """
        products.sort()
        res=[]
        l,r=0,len(products)-1
        for i in range(len(searchWord)):
            letter=searchWord[i]
            #check whether this letter is present at that index of not
            while l<=r and (len(products[l])<=i or products[l][i]!=letter):
                l+=1
            #check from back
            while l<=r and (len(products[r])<=i or products[r][i]!=letter):
                r-=1
            
            window=r-l+1
            res.append([]) #new list
            for i in range(min(3,window)):
                res[-1].append(products[l+i])
        return res