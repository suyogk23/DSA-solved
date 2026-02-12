class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        #TC: O(n)
        #Space: O(n)
        n = len(strength)
        MOD = 10**9 + 7

        # finding the left and right smaller element than element at index i
        left_smaller = [-1]*n
        monostk = [] 
        for i in range(n):
            while monostk and strength[i] <= strength[monostk[-1]]:
                monostk.pop()
            left_smaller[i] = monostk[-1] if monostk else -1
            monostk.append(i)
           

        right_smaller = [n]*n
        monostk = []
        for i in range(n-1, -1, -1):
            while monostk and strength[i] < strength[monostk[-1]]:   # to avoid duplicates
                monostk.pop()
            right_smaller[i] = monostk[-1] if monostk else n
            monostk.append(i)
            
        # calculate prefix sum and prefix of prefix sum
        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD
        
        # Prefix of prefix sums
        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = (prefix_prefix[i] + prefix[i]) % MOD

        # this part is used to calculate the strength of all subarrays where strength[i] is minimum
        total_strength = 0
        for i in range(n):
            left = left_smaller[i]+1 # idx
            right = right_smaller[i]-1 # idx

            # get sum of all subarrays from left-1..i  and i..right-1                
            left_sum = (prefix_prefix[i+1] - prefix_prefix[left]) % MOD
            left_sum = (left_sum * (right-i+1))% MOD

            right_sum = (prefix_prefix[right+2] - prefix_prefix[i+1]) % MOD
            right_sum = (right_sum * (i-left+1)) % MOD

            cur_strength = (right_sum - left_sum) % MOD
            cur_strength = cur_strength * strength[i] % MOD

            total_strength += cur_strength % MOD
        
        return total_strength % MOD



 
