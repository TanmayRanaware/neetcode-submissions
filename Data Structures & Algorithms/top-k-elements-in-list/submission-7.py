class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(nlogn)
        d={}
        for num in nums:
            d[num]=d.get(num, 0) +1
        return sorted(set(nums), key = lambda num: d[num])[-k:] 


        # o(klogn)
        d={}
        for num in nums:
            d[num]=d.get(num, 0) +1
        max_heap=[]
        for num in d:
            heapq.heappush(max_heap, (-d[num], num))
        heapq.heapify(max_heap) #o(N)
        res=[]
        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1]) # pop- o(logn)
        return res   

        #O(n) time 
        freq_to_num_dict={i:set() for i in range(len(nums)+1)}
        num_to_freq_dict={}
        for num in nums:
            freq = num_to_freq_dict.get(num, 0) + 1
            num_to_freq_dict[num] = freq
            if num in freq_to_num_dict[freq-1]:
                freq_to_num_dict[freq-1].remove(num)
            freq_to_num_dict[freq].add(num) 

        res=[]
        for freq in range(len(nums), 0, -1):
            if k<=0:
                break
            if k >= len(freq_to_num_dict[freq]):
                res.extend(freq_to_num_dict[freq])
                k-= len(freq_to_num_dict[freq])
                continue

            while k > 0 and k < len(freq_to_num_dict[freq]): 
                   res.append(freq_to_num_dict[freq].pop())
                   k-=1
        return res           

            







        