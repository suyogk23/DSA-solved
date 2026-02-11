class Solution:
    def largestVariance(self, s: str) -> int:
        # TC: O(n)  ->  O(n * 26 * 26) + O(n)
        # Space: O(1)
        # get counts of all characters in s, apply modified kadance algorith to each combination of char except both same characters
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        # modified kadane's algorithm to find max variance between 2 characters
        def findMaxVariance(major, minor):
            major_count = minor_count = 0
            rem_minor = count[minor]
            global_max = 0
            
            for c in s:
                if c == major:
                    major_count += 1
                if c == minor:
                    minor_count += 1
                    rem_minor -= 1

                if minor_count > 0: # because we need both major and minor char to be present n substring to find variance
                    cur_variance = major_count - minor_count
                    global_max = max(global_max, cur_variance)
                # if minor > major count, we have negative variance, discard the subarray if there 
                # are still remaining minors in the subarray
                if major_count < minor_count and rem_minor > 0:
                    # reset, discard previous subarray
                    major_count = minor_count = 0
   
            return global_max

        # find max variance between all unique characters in s, with each character assigned as major and minor and the opposite
        chars = list(count.keys())
        n = len(chars)
        max_variance = 0

        for i in range(n):
            for j in range(n):
                if i != j:
                    cur_variance = findMaxVariance(chars[i], chars[j]) 
                    max_variance = max(max_variance, cur_variance)

        return max_variance



