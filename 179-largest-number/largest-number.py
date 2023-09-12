class largerKey(str):
    def __lt__(x,y):
        return x+y>y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #comparing 
        #for i, n in enumerate(nums):
        #   nums[i]=str(n)
        def compare(n1,n2):
            if n1+n2>n2+n1:
                return -1 # return n1 at start
            else:
                return 1
        nums=list(map(str,nums))
        nums=sorted(nums,key=cmp_to_key(compare))
        return str(int("".join(nums)))

        largest_num=''.join(sorted(map(str,nums),key=largerKey))
        return '0' if largest_num[0]=="0" else largest_num
        