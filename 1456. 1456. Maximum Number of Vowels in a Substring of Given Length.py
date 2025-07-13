class Solution:
    """
    Use sliding window:
    1. init the array and count max vow
    2. use sliding window and calculate subsequent max vows
    3. if max vow == k, return as it is max possible
    4. else return max vow after entire array has been iterated
    This is O(n) solution
    """
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        n = len(s)
        max_vow = 0 
        for i in range(0, k):
            if (s[i] in vowels):
                max_vow+=1

        vow = max_vow
        i=k
        while(i < n):
            if (s[i-k] in vowels):
                vow-=1
            if (s[i] in vowels):
                vow+=1
            if vow == k:
                return vow
            max_vow = max(max_vow, vow)
            i+=1
        
        return max_vow
            

        
