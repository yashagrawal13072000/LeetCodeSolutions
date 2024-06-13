# There are n seats and n students in a room. You are given an array seats of length n, where seats[i] is the position of the ith seat.
# You are also given the array students of length n, where students[j] is the position of the jth student.

# You may perform the following move any number of times:

# Increase or decrease the position of the ith student by 1 (i.e., moving the ith student from position x to x + 1 or x - 1)
# Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

# Note that there may be multiple seats or students in the same position at the beginning.

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)
        n = len(seats)
        i=0

        while i<n:
            if sorted_seats[i] != sorted_students[i]:
                a = abs(sorted_seats[i] - sorted_students[i])
                result += a
                i+=1
        return result