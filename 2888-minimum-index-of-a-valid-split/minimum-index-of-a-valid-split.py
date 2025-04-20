class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        we want to majority element first
        and slide the index to find majority on both side and give the index 
        we can use voting algo here
        1.find majority element and count O(n)
        2.find on both side and give index O(n) so O(n) and space is O(1)
        """
        #find majority
        majority=nums[0]
        count=0
        for n in nums:
            if count==0:
                #we got new majority
                majority=n
            count += (1 if n==majority else -1)
        left_c=0
        right_c=nums.count(majority)
        for i in range(len(nums)):
            if nums[i]==majority:
                left_c+=1
                right_c-=1
            if 2*left_c > i+1 and 2*right_c > len(nums)-1-i:
                return i
        return -1
