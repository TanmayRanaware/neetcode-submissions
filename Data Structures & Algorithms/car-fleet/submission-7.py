from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [(target - p) / s for p, s in cars]

        fleet_count = 0
        merged = [False] * len(times)

        for i in range(len(times) - 1, -1, -1):
            if merged[i]:
                continue

            fleet_count += 1
            fleet_time = times[i]

            for j in range(i , -1, -1):
                if not merged[j] and times[j] <= fleet_time:
                    merged[j] = True

        return fleet_count