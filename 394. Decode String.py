'''
Use recursion
- for each substring inside bracket repeat same problem (subproblems)
for char in string:
    if char is digit:
        ans += k * string inside square brackets []
    else:
        until digit is found iterate
        ans += char until digit
return ans
'''
class Solution:
    def decodeString(self, s: str) -> str:
        i, n = 0, len(s)
        ans = ""
        while i < n:
            if s[i].isdigit():
                start = i
                while i < n and s[i+1].isdigit():
                    i+=1
                # print(s[start:i+1])
                k = int(s[start:i+1])
                closed = 1
                j = i+2
                while j < n and closed > 0:
                    if s[j] == ']':
                        closed -= 1
                    elif s[j] == '[':
                        closed += 1
                    j+=1
                ans += k*self.decodeString(s[i+2:j-1])
                i = j
            else:
                j = i
                while j < n and not s[j].isdigit():
                    j+=1
                ans += s[i:j]
                i = j
        return ans
            
