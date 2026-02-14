class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # O(n) + O(k)
        # maintian local maxima in lrft end of queue
        # maintain a double eneded queue monotonic decreasing from left to right
        # as we slide the window, the left end of q will have max ele index in window
        # in case this index falls out of window we pop element from left until it falls in the window again 
        # on the right side we append only elements lesser than current right element(ater poping from left)
        # if cure element is greater we pop until it is <= right element or until the queue is empty
        # we add the current element if it is ssmaller than right else we just skip adding current element
        # to gain intution DRAW a downward SLOPE GRAPH with overlapping windows to check why we do this 
        # IN SHORT: in q LEFT end CONTAINS current window MAX, the q stores subsequent idx in monotonic decreasing order
        n = len(nums)
        q = deque() # mono decreasing double ended queue, eg: [3,2,1]
        ans = []
        # handle first window
        for i in range(k):
            # remove elements < current ith element from right end 
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            # add current element to the right if q is empty of right end is >= cur element
            if not q or nums[q[-1]] >= nums[i]:
                q.append(i)
        ans.append(nums[q[0]])

        for i in range(k, n):
            # remove elements from left end if they are out of current window
            if q and q[0] < (i - k + 1): # each index can be added or popped atmost once so it is O(1)
                q.popleft()
            # remove elements < current ith element from right end 
            while q and nums[q[-1]] < nums[i]: # each index can be added or popped atmost once so it is O(1)
                q.pop()
            # add current element to the right if q is empty of right end is >= cur element
            if not q or nums[q[-1]] >= nums[i]:
                q.append(i)
            ans.append(nums[q[0]])
        
        return ans
            


