class Solution:
    def minSwaps(self, s: str) -> int:
        # TC: O(n)
        # Space: O(n)
        # generate valid string stating with 0 or 1, count number of zeros in s, then in generated strings count numof misplaces zeroes,
        # if num of zeroes matches in generated and original string do return the minimum swaps out of the 2 generated strings
        # NOTE: you need to check the num of zeroes for both the generated strings, because if the length is odd then numof zeroes and 1s may vary

        n = len(s)

        # generate valid strs
        s0 = 
        s1 = 
        # starting with 0
        c = '0'
        for i in range(n):
            s0 = s0 + c
            if c == '0':
                c = '1'
            else:
                c = '0'
        # starting with 1
        c = '1'
        for i in range(n):
            s1 = s1 + c
            if c == '0':
                c = '1'
            else:
                c = '0'
        # get count of 0 or 1
        count0 = 0
        for c in s:
            if c == '0':
                count0 += 1
        # check if str is valid by checking count of either 0 or 1 is valid and also get the min swap required
        def getSwapCount(st):
            swap_count = 0
            zero_count = 0
            for i in range(n):
                if st[i] == '0':
                    zero_count += 1
                    if st[i] != s[i]:
                        swap_count += 1
            return swap_count, zero_count

        swap_count0, zero_count0 = getSwapCount(s0)
        swap_count1, zero_count1 = getSwapCount(s1)

        if zero_count0 == count0 and zero_count1 == count0:
            return min(swap_count0, swap_count1)
        if zero_count0 == count0:
            return swap_count0
        if zero_count1 == count0:
            return swap_count1

        return -1
        

        # 0 1 0 1
        # 1 0 1 0
