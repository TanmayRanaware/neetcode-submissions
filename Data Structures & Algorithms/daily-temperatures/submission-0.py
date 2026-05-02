class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[-1]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
            while len(stack)!=0:
                top=stack[-1]
                if top[1]<temp:
                    res[top[0]]=i-top[0]
                    stack.pop()
                else:
                    break    


            stack.append((i,temp)) 
        while len(stack)!=0:
            top=stack[-1]
            res[top[0]]=0
            stack.pop()
        return  res      

