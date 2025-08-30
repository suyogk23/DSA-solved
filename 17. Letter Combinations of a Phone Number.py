class Solution:
    # soultion by @suyogk23 GITHUB
    # make a keypad map
    # for each digit:
    # backtrack: base case, if i >= n then append to ans, else 
    # backtrack on i+1 and ch + current_letter
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs",
            '8':"tuv", '9':"wxyz"
        }

        n = len(digits)
        if n <= 0:
            return []

        def dfs(i, ch):
            if i >= n:
                ans.append(ch)
                return
            for letter in map[digits[i]]:
                dfs(i+1, ch+letter)
        
        ans = []
        dfs(0, "")
        return ans
            
