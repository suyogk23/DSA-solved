class Solution:
    # solution by @suyogk23@GITHUB
    # convert all the numbers into tring binary representation
    # take care of prefix bits (extra zeros '0') 
    # finally calculate the number of flips
    # note: A[i] == '1' and B[i] == '1' and C[i] == '0' condition requires 2 flips, every other confition requires 1 flip
    # return number of required flips
    def minFlips(self, a: int, b: int, c: int) -> int:
        def binerize(num):
            bits = ''
            while num != 0:
                bits = str(num%2) + bits
                num //= 2
            if bits == '':
                return '0'
            return bits
        A = binerize(a)
        B = binerize(b)
        C = binerize(c)
        # append prefix bits
        la, lb, lc = len(A), len(B), len(C)
        maxl = max(la, lb, lc)
        if la == maxl:
            B = '0'*(la-lb) + B
            C = '0'*(la-lc) + C
        elif lb == maxl:
            A = '0'*(lb-la) + A
            C = '0'*(lb-lc) + C
        else:
            A = '0'*(lc-la) + A
            B = '0'*(lc-lb) + B
        #calculate flips
        flips = 0
        for i in range(maxl):
            ai, bi, ci = A[i], B[i], C[i]
            if (int(ai) or int(bi)) != int(ci):
                if A[i] == '1' and B[i] == '1' and C[i] == '0':
                    flips += 2
                else:
                    flips += 1
        return flips

        

        
