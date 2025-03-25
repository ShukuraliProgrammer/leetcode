from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        current_interval = intervals[0]

        result = []
        print("Current: ", current_interval)
        for interval in intervals[1:]:
            print(":crrent:", current_interval)
            if interval[0] <= current_interval[1]:

                current_interval[1] = max(current_interval[1], interval[1])

            else:
                # No overlap, add the current meeting to the result
                result.append(current_interval)
                current_interval = interval
        result.append(current_interval)
        return result

res = Solution()
intervals = [[1,4],[0,2],[3,5]]
print(res.merge(intervals))