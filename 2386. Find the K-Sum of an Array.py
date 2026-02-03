class Solution:
    # principle: if u have sum 10 from ele 1 + 2 + 3 + 4
    # next smallest sum will be: [2 + 3 + 4] excl[1] = 9
    # next smallest sum will be: [1 + 3 + 4] excl[2] incl[1] = 8
    # next smallest sum will be: [1 + 3 + 4] excl[2, 1] = 7
    # next smallest sum will be: [1 + 2 + 4] excl[3] incl[2] = 7
    # ---- storing above values with idx of sorted array in max heap will auto choose the next largest sum
    # ides for next largest sum: find the next 2 largest possible sum
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # find largest sum by considering only positive numbers
        largest_sum = 0
        for num in nums:
            if num > 0:
                largest_sum += num
        # sort and store the abs vals in the nums array
        abs_nums_sorted = sorted(abs(i) for i in nums)
        max_heap = [(-largest_sum, 0)] 
        # abs_nums_sorted has the smallest nums we can subtract from nums arr
        # for each element in max_heap.pop(): 
        # we remove the cur abs_nums_sorted[i] and push it to heap
        # we also add abs_nums_sorted[i-1] and remove

        # NOTE  since we are using -ve vals in minheap to act as max heap, + and - operations are used interchangeably
        for _ in range(k):
            cur_sum, idx = heapq.heappop(max_heap)
            if idx < n:
                heapq.heappush(max_heap, (cur_sum + abs_nums_sorted[idx], idx+1))
                if idx > 0:
                    heapq.heappush(max_heap, (cur_sum - abs_nums_sorted[idx-1] + abs_nums_sorted[idx], idx+1))

        return -cur_sum
        

