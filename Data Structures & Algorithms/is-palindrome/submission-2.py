class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1
        # s=''.join(c if c.isalnum() else '' for c in s.lower())
        # return s==s[::-1]

        # 2
        # l,r=0,len(s)-1
        # while l<r:
        #     while l<r and not s[l].isalnum():
        #         l+=1
        #     while l<r and not s[r].isalnum():
        #         r-=1
        #     if(s[l].lower()!=s[r].lower()):
        #         return False    
        #     l+=1
        #     r-=1
        # return True 

        # 3 
        s=''.join(c if c.isalnum() else '' for c in s)  
        l, r = 0,len(s)-1
        while l<r:
            if(s[l].lower()!=s[r].lower()):
                return False
            l+=1
            r-=1    
        return True    

        