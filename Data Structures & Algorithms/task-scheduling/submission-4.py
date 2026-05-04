class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        last_used={}
        time=0
        while freq:
            time+=1
            best_task=None
            for task in tasks:
                if task not in last_used:
                    if best_task==None or freq[task]>freq[best_task]:
                        best_task=task
                else:
                    if time-last_used[task]>n and freq[task]>freq[best_task]:
                        best_task=task
            if best_task:
                freq[best_task]-=1
                last_used[best_task]=time
                if freq[best_task]==0:
                    del freq[best_task]
        return time        

                        


                        
                        

