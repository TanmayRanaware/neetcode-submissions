class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    #     self.res=[]
    #     self.subset=[]
    #     self.dfs(0, nums)
    #     return self.res
    # def dfs(self, i, nums):
    #     if i==len(nums):
    #         self.res.append(self.subset.copy())
    #         return
    #     self.subset.append(nums[i])
    #     self.dfs(i+1, nums)

    #     self.subset.pop()
    #     self.dfs(i+1, nums) 
    #iterative
        res=[[]]
        for num in nums:
            new_subset=[]
            for res_subset in  res:
                new_subset.append(res_subset+[num])
            res.extend(new_subset) 
        return res          

