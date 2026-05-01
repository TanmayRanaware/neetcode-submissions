class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        mul_prefix=1
        for i in range(len(nums)):
            mul_prefix*=nums[i]
            prefix[i]=mul_prefix
        print(f"{prefix}")   


        mul_suffix=1
        suffix=[1]*len(nums)
        for j in range(len(nums)-1,-1,-1):
            mul_suffix*=nums[j]
            suffix[j]=mul_suffix
        print(f"{suffix}")     

        res=[suffix[1]]
        for index in range(1, len(nums)-1):
            res.append(suffix[index+1]*prefix[index-1])
        res.append(prefix[len(nums)-2]) 
        return res   

        

        