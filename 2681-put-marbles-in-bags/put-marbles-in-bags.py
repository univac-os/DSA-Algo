class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        we want to split the array and take first and last value in that each split
        looking at this we will always have wt[0] and wt[-1] present in our max and min and we want to take splits
        so how to take the spilit 
        assume nums in sort max 1 2 3 4 5 6 7 we want 2 split 
        max= 1+ 7 --> if i make split at 6 1..6 7 so 1 + 6+7 + 7
        min =1+7 --> if i make split at 2 1..1 2...7 so 1 + 1+2 + 7
        now if i want 3 split 
        max =1+7 --> 1..5 6 7 so 1+ 5+6+6+7+  7
        min =1+7 --> 1..1 2 3..7 1+ 1+2+2+3+  7
        how to get the split here simple each split at each index and get the adj sum values
        """
        if k==1 or len(weights)<=k:return 0
        splits=sorted([weights[i-1]+weights[i] for i in range(1,len(weights))])
        maxi=weights[0]+ sum(splits[-(k-1):]) +weights[-1]
        mini=weights[0]+sum(splits[:(k-1)]) +weights[-1]
        return maxi-mini
