class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #create a set of num1 and check whether that value is present in nums2 O(n) space-O(n)
        #but set will have unique value only so use hashmap and count O(n) and space - O(n)
        nums1=Counter(nums1)
        res=[]
        for n in nums2:
            if n in nums1 and nums1[n]>0:
                res.append(n)
                nums1[n]-=1
        return res

