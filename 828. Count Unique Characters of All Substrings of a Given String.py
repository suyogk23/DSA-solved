class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Time: O(n) + O(26): O(n)
        # Space: O(26): O(1)
        # count the number of substr combination where a s[i] can be unique
        n = len(s)
        char_idx = {}
        res = 0

        for i, c in enumerate(s):
            if c not in char_idx:
                char_idx[c] = [-1, -1]
            
            j, k = char_idx[c]
            res += (k - j) * (i - k)
            char_idx[c] = [k, i]

        # edge case for all the unique chars and char that s at n-1 idx
        for j, k in char_idx.values():
            res += (k - j) * (n - k)

        return res
        
        
            
        
