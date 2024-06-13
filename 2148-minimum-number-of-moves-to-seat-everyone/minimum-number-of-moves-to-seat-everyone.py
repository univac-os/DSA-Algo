class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        #sort both and get the diff --GREEDY O(nlogn)
        #use counting sort and check each one --> O(n)
        #but give n can be max of 100 so O(n)=O(nlogn)
        seats.sort()
        students.sort()
        res=0
        for i in range(len(seats)):
            res+=abs(seats[i]-students[i])
        return res