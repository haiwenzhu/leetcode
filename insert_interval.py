# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        res = []
        for i, interval in enumerate(intervals):
            if interval.end < newInterval.start:
                res.append(interval)
            elif interval.start > newInterval.end:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            else:
                newInterval.start = min(newInterval.start, interval.start)
                newInterval.end = max(newInterval.end, interval.end)
        res.append(newInterval)
        return res

if __name__ == "__main__":
    solution = Solution()
    vals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    intervals = []
    for item in vals:
        intervals.append(Interval(item[0], item[1]))
    newInterval = Interval(4,9)
    res = solution.insert(intervals, newInterval)
    print([(item.start, item.end) for item in res])
