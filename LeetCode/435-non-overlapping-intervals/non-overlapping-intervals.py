class Solution:
    def eraseOverlapIntervals(seelf, intervals):
        intervals.sort(key=lambda x: x[1])
    
        count_non_overlap = 0
        last_end = float('-inf')
    
        for start, end in intervals:
            if start >= last_end:
                count_non_overlap += 1
                last_end = end
    
        return len(intervals) - count_non_overlap

        