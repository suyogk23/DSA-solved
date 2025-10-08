class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # solution by @suyogk23 GITHUB
        # Both small and bif str should be divisible by the substr (even their lengths)
        # the substr should be <= small str only
        # start the check from entire small str as substr and consecutively reduce its len from right (check only prefixes)
        def getGCD(smallStr, largeStr):
            n = len(largeStr)
            m = len(smallStr)
            for i in range(m, 0, -1):
                if n%i == 0 and m%i==0:
                    substr = smallStr[0:i]
                    if (n//i)*substr == largeStr and (m//i)*substr == smallStr:
                        return substr
            return ""
        
        if len(str1) > len(str2):
            return getGCD(str2, str1)
        else:
            return getGCD(str1, str2)
