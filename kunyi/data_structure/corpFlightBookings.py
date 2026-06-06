class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # first sort the bookings 
        # [1, 2] + 10 => diff[1] + 10, dff[3] - 10 
        updates_for_flight = [0] * (n + 1)
        for first, last, seats in bookings:
            updates_for_flight[first - 1] += seats
            updates_for_flight[last] -= seats 
        
        #cumulative sum processing (prefix)
        running = 0
        result = []
        for i in range(n):
            running += updates_for_flight[i]
            result.append(running)

        return result
        
