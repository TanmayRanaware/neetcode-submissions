class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #sorting- tc:o(nlogn)
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        return points[:k]

        #heap:
        #Time: O(n + k log n) if heapified, or O(n log n + k log n) with pushes
        heap=[]
        for x,y in points:
            dist=x*x + y*y
            heapq.heappush(heap, (dist, x, y))
        res=[]    
        for i in range(k):
            dist,x,y = heapq.heappop(heap)
            res.append([x,y])
        return res        

        