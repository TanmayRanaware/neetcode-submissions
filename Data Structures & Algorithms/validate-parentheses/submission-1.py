class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_paranthesis=["(","{","["]
        closed_paranthesis=[")","]","}"]
        open_to_closed={
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for char in s:
            if char in open_paranthesis:
                stack.append(char)
            else:
                if len(stack)==0 or open_to_closed[stack[-1]] != char:
                    return False
                stack.pop()  
        return len(stack)==0        