class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left=0
        # last_seen=[-1]*128
        # res=0
        # for right in range(len(s)):
        #     c = s[right]
        #     if last_seen[ord(c)]>=left:
        #         left=last_seen[ord(c)]+1
        #     last_seen[ord(c)]=right
        #     res=max(res,right-left+1)
        # return res

        #sliding window
        seen=set()
        left=0
        n=len(s)
        res=0
        for right in range(n):
            while right>left and s[right] in seen:
                seen.remove(s[left])
                left+=1
                
            seen.add(s[right])
            res=max(res, right-left+1)
        return res        
                 


        