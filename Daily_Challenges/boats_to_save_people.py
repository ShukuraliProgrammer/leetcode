from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the list
        sorted_people = sorted(people)
        left = 0  # Pointer to the start of the list
        right = len(sorted_people) - 1  # Pointer to the end of the list
        boat_counter = 0

        while left <= right:
            # If the heaviest and lightest person can fit in the same boat
            if sorted_people[left] + sorted_people[right] <= limit:
                left += 1  # Move the left pointer to the next person
            right -= 1  # Always move the right pointer (heaviest person)
            boat_counter += 1  # Increment boat count

        return boat_counter




bout_counter = Solution()
people = [4,3,6]
limit = 6
print(bout_counter.numRescueBoats(people, limit))


