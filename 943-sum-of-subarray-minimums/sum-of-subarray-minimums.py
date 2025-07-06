class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #O(n2) make each subarray and keep check of minimum and give that value
        #O(n)- we maintain monotonic Increasing stack 
        #here if we get minimum value then if next incoming elements are greater than this,we wont take it
        #if incoming is minimim value then prev value is mini val for those subarray
        #looks dp
        MOD=10**9+7
        n,res=len(arr),0
        stack=[] #(idx)
        #find num in subarray where it is minimum
        for right in range(n+1):
            while stack and (right==n or arr[stack[-1]]>=arr[right]):
                #pop it and calculate the min the num present in subarry
                mid=stack.pop()
                left=stack[-1] if stack else -1 #start point
                res=(res+arr[mid]*(mid-left)*(right-mid))%MOD
            stack.append(right)
        return res


        res=0
        stack=[]#(index,num)
        for idx,n in enumerate(arr):
            while stack and n<stack[-1][1]:
                #we got new mini val
                prev_idx,prev_val=stack.pop()
                #now get those subarray with this mini val
                #left --go till that prev val in stack OR if prev_idx is 1 them left is 2 index->[1,[0,1]]
                #right -prev_idx to now  
                left=prev_idx -stack[-1][0] if stack else prev_idx+1
                right=idx-prev_idx
                #add to res combinations
                res=(res + prev_val*left*right)%MOD
            stack.append((idx,n))
            
        #NOW we got the mono stack now take each one and calculator the combination
        for i in range(len(stack)):
            idx,val=stack[i]
            left=idx - stack[i-1][0] if i>0 else idx+1
            right=len(arr)-idx #till last we take combination
            res=(res+ val*left*right)%MOD
        
        return res
        