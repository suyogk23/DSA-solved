class Solution:
    # solution by @suyogk23 GITHUB
    # tradtitional string processing
    # use a while loop and store words in array and ignore spaces
    # now append the words in the array in reverse order
    # return the string
    def reverseWords(self, s: str) -> str:
        i, n = 0, len(s)
        words = []
        while i < n:
            word = ''
            while i < n and s[i] != ' ':
                word = word + s[i]
                i+=1
            if word:
                words.append(word)
            i+=1
        ans = ''
        for word in words:
            ans = word + " " + ans
        
        ans = ans[:-1]
        return ans

            
