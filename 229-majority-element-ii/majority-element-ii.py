class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #1.count for each one O(n2) 
        #2. use hashmap and check count  O(n)
        #3. Demi-moore voting algo  O(n) space is O(1) 
        #   we need val > n/3 so think of election a person with more than 33% wins
        #  assume everyone get 33 + 33 +33 so remaining will be 1 given to anyone so winner is 1
        # assume assume 33 + 33 so remaing votes gets scattered to independent and few get to 1st and 2nd say 35 + 37 so 100/3 =33.33 so 35 and 37 is more so 2 people are there
        if not nums:
            return []
        c1,c2,n1,n2=0,0,random,random
        for n in nums:
            if n==n1:
                c1+=1
            elif n==n2:
                c2+=1
            elif c1==0:
                n1=n #new member is more than previous one
                c1=1
            elif c2==0:
                n2=n
                c2=1
            else:
                #votes are scattered
                c1-=1
                c2-=1

        #now we got vote count check who are in majority check greater than n//3
        return [n for n in (n1,n2) if nums.count(n)>len(nums)//3]
        