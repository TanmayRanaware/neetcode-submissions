class Solution:
    def isHappy(self, n: int) -> bool:
        strn=str(n)
        visited=set()
        while strn not in visited:
            visited.add(strn)
            strn=str(sum(pow(int(digit),2) for digit in strn))
            if strn=="1":
                return True
        return False
        