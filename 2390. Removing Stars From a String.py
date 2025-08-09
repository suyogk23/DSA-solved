class Solution:
"""
if other char puth it to stack, if * encountered pop from stack if stack is not
empty, return stack as string
"""
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        
        return "".join(stack)
