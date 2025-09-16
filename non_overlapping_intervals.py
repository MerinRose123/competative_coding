"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""
"""
Approach 2 : Greedy, Sort from end
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        count_non_overlap = 1  # always keep the first one
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:  # no overlap → keep
                count_non_overlap += 1
                prev_end = end

        # Total intervals - max non-overlap = min removals
        return len(intervals) - count_non_overlap
"""
Approach 2 : Greedy, Sort from start. 
Sort from start is optimal for merging intervals. In this question this is more complex.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        result = 0
        currentMax = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < currentMax:  # overlap
                result += 1
                # Keep the interval with smaller end
                currentMax = min(currentMax, intervals[i][1])
            else:
                # No overlap → update boundary
                currentMax = intervals[i][1]

        return result
