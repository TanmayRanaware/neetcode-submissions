class Solution:
    # brute- 
    # Total strings generated: 2^(2n) = 4^n
    # Each validity check costs O(n)
    # Time: O(n * 4^n)
    # Space: O(n) recursion, excluding output
    # def isValid(self, ch):
    #     balance=0
    #     for c in ch:
    #         if c=='(':
    #             balance+=1
    #         else:
    #              balance-=1 
    #         if  balance<0:
    #             return False
    #     return balance==0          

    # def combinations(self, res, ch, n):
    #     if len(ch)==2*n:
    #         if self.isValid(ch):
    #             res.append(ch)
    #         return     
    #     self.combinations(res, ch+'(', n)
    #     self.combinations(res, ch+')', n) 


    # def generateParenthesis(self, n: int) -> List[str]:
    #     res=[]
    #     self.combinations(res, "", n)
    #     return res

    # optimal
    def backtrack(self, n, cur, res, open_count, closed_count):
        if len(cur)==2*n:
            res.append(cur)
            return
        if open_count < n :
            self.backtrack(n, cur+"(", res, open_count+1, closed_count)
        if closed_count < open_count:
            self.backtrack(n, cur+")", res, open_count, closed_count+1)    


    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.backtrack(n, "", res, 0,0)
        return res


        