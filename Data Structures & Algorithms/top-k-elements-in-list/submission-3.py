class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(nlogn)
        # d={}
        # for num in nums:
        #     d[num]=d.get(num, 0) +1
        # return sorted(set(nums), key = lambda num: d[num])[-k:] 


        d={}
        for num in nums:
            d[num]=d.get(num, 0) +1
        max_heap=[]
        for num in d:
            heapq.heappush(max_heap, (-d[num], num))

        heapq.heapify(max_heap) #o(N)
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res    



        