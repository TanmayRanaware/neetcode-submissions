from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed),  key=lambda x: x[0])
        times = [(target - p) / s for p, s in cars]

        fleets = []  

        for i in range(len(times) - 1, -1, -1):
            curr_time = times[i]
            j = 0
            merged = False

            while j < len(fleets):
                if curr_time <= fleets[j]:
                    merged = True
                    break
                j += 1

            if not merged:
                fleets.insert(0, curr_time)

        return len(fleets)