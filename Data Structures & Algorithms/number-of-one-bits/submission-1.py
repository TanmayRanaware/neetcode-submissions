class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        for bit in bin(n):
            count+=1 if bit=='1' else 0
        return count    


        