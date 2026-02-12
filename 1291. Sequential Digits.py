class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # TC: O(D + D*9) = O(1) as max possible num of digits D is 9 (constant)
        # space: O(D*9) = O(1) as max possible num of digits D is 9 (constant)
        if low > high:
            return []
        ans = []
        l = low
        h = high
        ld = hd = 1
        # get first digit of low
        while l//10 > 0:
            l = l//10
            ld += 1
        # get first digit of hight
        while h//10 > 0:
            h = h//10
            hd += 1
        digit = l
        # generate sequences
        for i in range(ld, hd+1):
            while digit <= 9 - i + 1:
                if i == hd and digit > h:
                    break
                num = 0
                for j in range(i):
                    num = num + digit + j
                    num = num * 10
                num = num // 10
                if num >= low and num <= high:
                    ans.append(num)
                digit += 1
            digit = 1

        return ans
        


