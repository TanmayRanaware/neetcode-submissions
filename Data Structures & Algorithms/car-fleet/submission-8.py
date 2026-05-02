from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # cars = sorted(zip(position, speed))
        # times = [(target - p) / s for p, s in cars]

        # fleet_count = 0
        # merged = [False] * len(times)

        # for i in range(len(times) - 1, -1, -1):
        #     if merged[i]:
        #         continue

        #     fleet_count += 1
        #     fleet_time = times[i]

        #     for j in range(i - 1, -1, -1):
        #         if not merged[j] and times[j] <= fleet_time:
        #             merged[j] = True           

        # return fleet_count

        #o(N) + o(nlogn) TIME 
        cars_time=[]
        for p,s in zip(position, speed):
            time=(target-p)/s
            cars_time.append((p, time))
        cars_time.sort(reverse=True) 
        fleet_time=0
        fleet_count=0
        for p,t in cars_time:
            if t>fleet_time:
               fleet_count+=1
               fleet_time=t
        return  fleet_count        


