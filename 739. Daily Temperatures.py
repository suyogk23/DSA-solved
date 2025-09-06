class Solution:
    # solution by @suyogk23 GITHUB
    # maintain a decreasing monotonic stack 
    # (monotonic stack will have elements from bottom to top in decreasing or increasing order)
    # when you encounter an element larger than stack top update the 
    # corresponding top idx in answer array 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = [] # ele(val, idx) # decreasing monotonic stack
        n = len(temperatures)
        ans = [0]*n

        for i in range(0, n):
            while(monoStack and monoStack[-1][0] < temperatures[i]):
                ans[monoStack[-1][1]] = i - monoStack[-1][1]
                monoStack.pop()
            else:
                monoStack.append((temperatures[i], i))
            
        return ans
