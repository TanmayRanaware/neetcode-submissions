class Solution:
    def __init__(self):
        self.memo={}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.minCostClimbingStairsDp(len(cost),cost)
    
    def minCostClimbingStairsDp(self, i, cost):
        if i<=1:
            return 0
        if i in self.memo:
            return self.memo[i]
        case1= self.minCostClimbingStairsDp(i-1,cost)+cost[i-1]
        case2=  self.minCostClimbingStairsDp(i-2,cost)+cost[i-2] 
        self.memo[i]=min(case1, case2)
        return self.memo[i]



        