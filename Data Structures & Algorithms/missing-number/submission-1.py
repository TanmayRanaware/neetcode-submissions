class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #o(n) time and O(n) space
        # visited= set(range(len(nums) + 1))
        # for num in nums:
        #     assert num in visited
        #     visited.remove(num)
        # assert len(visited)==1
        # return visited.pop()  

        #O(n) time and O(1) space  
        xor_num=0
        for num in nums:
            xor_num ^= num
        for i in range(len(nums)+1):
            xor_num^=i
        return  xor_num      

        