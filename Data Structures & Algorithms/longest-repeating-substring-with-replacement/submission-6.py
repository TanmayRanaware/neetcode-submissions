class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=[0]*26
        l=0
        maxFreq=0
        best=0
        for r in range(len(s)):
            ch=s[r]
            index=ord(ch)-ord('A')
            freq[index]+=1
            maxFreq=max(maxFreq, freq[index])
            if r-l+1 - maxFreq > k:
                freq[ord(s[l])-ord('A')]-=1
                l+=1
                maxFreq=0
                for i in range(l,r+1):
                    maxFreq=max(maxFreq, freq[ord(s[r])-ord('A')])
            else:
                best=max(best, r-l+1)
            freq    
        return best        

           



        