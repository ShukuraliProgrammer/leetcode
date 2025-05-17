from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        difference_days = 0
        meetings.sort(key=lambda x: x[0])

        merged_meetings = []

        # Initialize with the first meeting
        current_meeting = meetings[0]

        for meeting in meetings[1:]:
            start, end = meeting
            current_start, current_end = current_meeting

            # Check if the current meeting overlaps with the next meeting
            if start <= current_end:
                # Merge the meetings by updating the end time
                current_meeting = [current_start, max(current_end, end)]
            else:
                # No overlap, add the current meeting to the result
                merged_meetings.append(current_meeting)
                current_meeting = meeting

        # Add the last meeting
        merged_meetings.append(current_meeting)

        difference_days = 0
        for meeting_2 in merged_meetings:
            difference_days += meeting_2[1] - meeting_2[0] + 1


        return days - difference_days

# Example usage
meetings = [[2,4],[1,3]]

exam1 = Solution()
print(exam1.countDays(5, meetings))