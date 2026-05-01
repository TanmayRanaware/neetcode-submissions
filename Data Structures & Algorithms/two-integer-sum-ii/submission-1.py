class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(numbers)):
            num=numbers[i]
            wanted=target-num
            if wanted in seen:
                return [seen[wanted]+1,i+1]
            seen[num]=i
        return [-1,-1]   
        