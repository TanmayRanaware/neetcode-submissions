class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        last_seen=[-1]*128
        res=0
        for right in range(len(s)):
            c = s[right]
            if last_seen[ord(c)]>=left:
                left=last_seen[ord(c)]+1
            last_seen[ord(c)]=right
            res=max(res,right-left+1)
        return res

        #sliding window
        seen={}
        left=0
        n=len(s)
        res=0
        for right in range(n):
            while s[right] in seen:
                left+=1
                seen.remove(s[left])
            seen.add(right)
            res=max(res, right-left+1)
        return res        
                 


        