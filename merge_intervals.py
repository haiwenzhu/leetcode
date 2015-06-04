# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    """
    @see https://leetcode.com/problems/merge-intervals/
    """
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda interval: interval.start)
        res = []
        item = None
        for interval in intervals:
            if not item:
                item = interval
            elif item.end >= interval.start:
                item.end = max(item.end, interval.end)
            else:
                res.append(item)
                item = interval
        if item:
            res.append(item)
        return res