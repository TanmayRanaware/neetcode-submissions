class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # time- o(n*max(piles))
        # for k in range(1, max(piles)+1):
        #     hours=0
        #     for pile in piles:
        #         hours+=math.ceil(pile/k)
        #     if hours<=h:
        #         return k

        #binary search 
        left=1
        right= max(piles)
        ans=0
        while left<=right:
            k=left+(right-left)//2
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)
            if hours<=h:
                ans=k
                right=k-1
            else:
                left=k+1
        return ans           

                   
