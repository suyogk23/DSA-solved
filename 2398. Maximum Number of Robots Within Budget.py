class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # TC: O(n)
        # Space: O(n)
        # slididng window to track maximum subarray
        # use a monotonic decreasting queue: [3, 2, 1] to track next maximum chargeTimes
        # this way we store only max elements in a queue as we move right, it wont matter if other elements are in left and not max
        # in case the left index == max_element index we can just pop it fom queue
        
        n = len(runningCosts)
        left = 0
        mono_dec_q = deque()
        cur_cost = 0
        ans = 0

        for i in range(n):
            # pop all elements smaller than cur element to maintain mono decreasing q
            while mono_dec_q and chargeTimes[mono_dec_q[-1]] <= chargeTimes[i]:
                mono_dec_q.pop()
            mono_dec_q.append(i)
            cur_cost += runningCosts[i]
            # shrink window to left
            while mono_dec_q and (chargeTimes[mono_dec_q[0]] + (i-left+1)*cur_cost) > budget:
                cur_cost -= runningCosts[left]
                if mono_dec_q[0] == left:
                    mono_dec_q.popleft()
                left += 1
        
            ans = max(ans, (i-left+1))
        
        return ans
