class Solution:
# Pattern: "Stack for collision/interaction problems"
# - Use a stack to maintain elements that are still valid/alive.
# - For each new element, compare with the stack top:
#     * While there is conflict → resolve it (pop from stack or discard current).
#     * If element survives all conflicts → push it to stack.
# - In Python, `while ... else` is a neat trick:
#     else runs only if no `break` occurs → meaning the new element survived.
# This pattern is common in problems like asteroid collision, 
# next greater element, parentheses validation, etc.
# solution by @suyogk23 GITHUB

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                if stack[-1] < abs(i):
                    stack.pop()
                    continue
                elif stack[-1] == abs(i):
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack



