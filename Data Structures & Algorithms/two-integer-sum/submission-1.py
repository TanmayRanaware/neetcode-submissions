class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            wanted=target-num
            if wanted in seen:
                return [seen[wanted],i]
            seen[num]=i
        return [-1,-1]                   