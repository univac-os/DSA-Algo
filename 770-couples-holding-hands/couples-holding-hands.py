class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        """
        we want pair in order (x,x+1) or(x+1,x) Linkedlist? No
        we have couple same as index values so index transveral? gives cycle but no use
        we need to swap the index position take 2 element at a time
        HOW can i know pair value say x=2 them pair is 3 so here if x is even pair is x+1 else x-1
        """
        n=len(row)
        pos={n:idx for idx,n in enumerate(row)} #hashmap
        res=0
        for i in range(0,n,2):
            first=row[i]
            partner=first+1 if first%2==0 else first-1
            if partner !=row[i+1]:
                #we need to swap
                partner_idx=pos[partner]
                #swap
                row[i+1],row[partner_idx]=row[partner_idx],row[i+1]
                #update pos 
                pos[row[partner_idx]],pos[row[i+1]]=partner_idx,i+1
                res+=1
        return res
