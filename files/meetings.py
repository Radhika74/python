class Solution:
    def countDays(self, days, meetings):
        result, end=0,0
        for start, e in sorted(meetings)+[[days+1]*2]:
            result += max(0,start-end-1)
            end = max(end,e)
        return result
    
days = 100
meetings = [[0,3],[5,10],[15,20]]
print(Solution().countDays(days, meetings))
