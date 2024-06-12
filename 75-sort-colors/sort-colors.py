class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #3 ptr appraoch check each number and move ptr
        ptr0=ptr1=0
        ptr2=len(nums)-1
        while (ptr1<=ptr2):
            #check for 0
            if (nums[ptr1]<1):
                nums[ptr1],nums[ptr0]=nums[ptr0],nums[ptr1]
                ptr1+=1
                ptr0+=1
            #check for 2
            elif nums[ptr1]>1:
                nums[ptr1],nums[ptr2]=nums[ptr2],nums[ptr1]
                ptr2-=1
            #check 1
            else:
                ptr1+=1
        return nums
        