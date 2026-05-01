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


        