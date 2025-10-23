class Solution:
    # solution by @suyogk23 GITHUB
    # you need to store num1[i] and num2[i] as pairs in an array and sort this array of pairs with respect to nums2[i]
    # in descending, as you need to keep track of max nums2[i], now find the corresponding 
    # nums1[i] sum and keep track of it, if n > k, then pop the minimum element from nums1[i] (note that since pair array is sorted in desc, there is no ned to track 
    # nums2[i] as it will always be lesser in subseq iters) and subtract it from the sum
    # keep track of max(sum * min(nums2[j])])
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = [(n1, n2) for n1, n2 in zip(nums1, nums2)]        
        arr.sort(key=lambda x:x[1], reverse=True) # sort the array with respect to second element in the tuple pair
        # print(arr)
        # find the max value attainable
        min_heap = []
        maxSum, ans = 0, 0
        for n1, n2 in arr:
            maxSum += n1
            heapq.heappush(min_heap, n1)
            if len(min_heap) > k:
                n = heapq.heappop(min_heap)
                maxSum -= n
            if len(min_heap) == k:
                ans = max(ans, maxSum*n2)
        return ans
