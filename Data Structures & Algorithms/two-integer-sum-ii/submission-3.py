class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #o(n) time and o(n) space
        seen={}
        for i in range(len(numbers)):
            num=numbers[i]
            wanted=target-num
            if wanted in seen:
                return [seen[wanted]+1,i+1]
            if num not in seen:
                seen[num]=i 
        return [-1,-1]   

        #O(n) time O(1) space
        l,r=0,len(numbers)-1
        while l<r:
            if numbers[l] + numbers[r] < target:
                l=l+1
            elif  numbers[l] + numbers[r]> target:
                r=r-1
            else:
                return [l+1,r+1] 
        return [-1,-1]          


        