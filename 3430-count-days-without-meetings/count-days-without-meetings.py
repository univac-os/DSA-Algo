class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        like meeting interval 
        merge interval and remove from days
        start is max of prev_end ,curr start
        end is max of prev_end,curr end
        """
        meetings.sort()
        prev_end=0
        for start,end in meetings:
            start=max(prev_end+1,start)
            end=max(prev_end,end)
            prev_end=max(prev_end,end)
            days-=(end-start+1)
        return days