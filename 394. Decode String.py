class Solution:
    # solution by @suyogk23 @GITHUB
    # use a stack
    # append to stack unless you encounter ']' (closing bracket)
    # when you encounter ']' (closing bracket)
    # pop substring until you encounter '[' opening bracket
    # now get the corresponding k (number), multiply it with the substring obtained
    # now push the resultant substring (num * sbstr) to stack
    # finally concatenate all the stes in stack and return the resultant string
    def decodeString(self, s: str) -> str:
        stk = []
        
        for c in s:
            if c == ']':
                # get the substr inside the bracket
                substr = ''
                while stk[-1] != '[':
                    substr = stk.pop() + substr # make sure you add char to substr in reverse order
                #pop off the opening bracket
                stk.pop()
                # get the number
                num = ''
                while stk and stk[-1].isdigit():
                    num += stk.pop()
                num = int(num[::-1]) # reverse the num
                stk.append(num * substr) 
            else:
                stk.append(c)
        ans = ""
        # concatenate all strings in the stack and return it
        for substr in stk:
            ans += substr
        return ans












