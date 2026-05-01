class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums=sorted(set(nums))
        if len(sorted_nums)==0:
            return 0
        longest=0
        l=1
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i]==sorted_nums[i-1]+1:
                l+=1    
            else:
                longest=max(longest, l)
                l=1
        return max(longest, l)        

                    
        