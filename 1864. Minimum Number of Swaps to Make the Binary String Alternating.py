class Solution:
    def minSwaps(self, s: str) -> int:
        # num0 and num1 diff > 1 then return -1
        # iteratively go from start 0 or 1
        # c=0, c=1, c=0 
        # c=1, c=0, c=1
        # compare c != s[i] if c==0

        # 110 # edge: count the num of 0 and 1 in generated seq
        # 101 # alternating 
        # 010 # not valid

        # Time: O(n)
        # Space: O(1)

        # get count of 0 and 1
        n = len(s)
        if n <= 1:
            return 0
        count0 = 0
        count1 = 0
        for c in s:
            if c=='0':
                count0 += 1
            else:
                count1 += 1
        # check if impossible to generate alternating string
        if (abs(count0-count1)) > 1:
            return -1
        
        def checkSwaps(c):
            num_swaps = 0
            for i in range(n):
                if c == 0:
                    # check the num of swaps
                    if s[i] != c:
                        num_swaps += 1
                    c = 1
                else:
                    c = 0
            return num_swaps

        # print((checkSwaps(0), checkSwaps(1)))
        if count0 > count1:
            return checkSwaps(0)
        elif count1 > count0:
            return checkSwaps(1)
        else:
            # 0s and 1s count are equal
            return min(checkSwaps(0), checkSwaps(1))
        

   

