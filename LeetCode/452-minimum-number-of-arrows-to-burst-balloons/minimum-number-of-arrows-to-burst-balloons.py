class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        last = float('-inf')
        count = 0
        for start, end in points:
            if start > last:
                count +=1
                last = end
        return count
