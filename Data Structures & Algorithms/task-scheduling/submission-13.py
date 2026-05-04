class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #brute-o(total_time*26) time
        # freq=Counter(tasks)
        # last_used={}
        # time=0
        # while freq:
        #     time+=1
        #     best_task=None
        #     for task in freq:
        #         if task not in last_used:
        #             if best_task==None or freq[task]>freq[best_task]:
        #                 best_task=task
        #         else:
        #             if time-last_used[task]>n and freq[task]>freq[best_task]:
        #                 best_task=task
        #     if best_task:
        #         freq[best_task]-=1
        #         last_used[best_task]=time
        #         if freq[best_task]==0:
        #             del freq[best_task]
        # return time    

        #heap- o(total_time*log26) time 
        freq=Counter(tasks)
        heap=[-f for f in freq.values()]
        heapq.heapify(heap)
        q=deque()
        time=0
        while heap or q:
            time+=1
            if heap:
                freq=heapq.heappop(heap)
                freq+=1
                if freq!=0:
                    q.append([freq,time+n])
            if q and q[0][1]==time:
                heapq.heappush(heap, q.popleft()[0])
        return time            




                        


                        
                        

