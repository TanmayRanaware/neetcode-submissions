class Solution:
    def isValid(self, ch):
        balance=0
        for c in ch:
            if c=='(':
                balance+=1
            else:
                 balance-=1 
            if  balance<0:
                return False
        return balance==0          

    def combinations(self, res, ch, n):
        if len(ch)==2*n:
            if self.isValid(ch):
                res.append(ch)
            return     
        self.combinations(res, ch+'(', n)
        self.combinations(res, ch+')', n) 


    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.combinations(res, "", n)
        return res

        