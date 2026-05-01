class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #o(nlogn)
        # sorted_nums=sorted(set(nums))
        # if len(sorted_nums)==0:
        #     return 0
        # longest=0
        # l=1
        # for i in range(1,len(sorted_nums)):
        #     if sorted_nums[i]==sorted_nums[i-1]+1:
        #         l+=1    
        #     else:
        #         longest=max(longest, l)
        #         l=1
        # return max(longest, l)  

        #o(n)
        longest=1
        nums=set(nums)
        if len(nums)==0:
            return 0
        for num in nums:
            #get 1st element of sequence
            if num-1 not in nums:
                x=num
                count=1
                while x+1 in nums:
                    count+=1
                    x+=1
                longest=max(longest, count)
        return longest        






                    
        