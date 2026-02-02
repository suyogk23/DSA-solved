class Solution:
    # use sliding window + backtracking
    # if s[l:r] is a word then you can choose to leave it or add it in your substring
    # else you can just leave it (always a case)
    # keep track of your substring length in cur_len
    # at end when r == n+1, if cur_len == len(s), return [se] else return []
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        
        def dfs(l, r, se, cur_len):
            if r == len(s)+1:
                if cur_len == len(s):
                    se = se.strip()
                    arr = [se]
                    return arr
                else:
                    return []
            not_take = dfs(l, r+1, se[:], cur_len)
            take = []
            if s[l:r] in wordDict:
                se = se + (s[l:r]) + ' '
                cur_len += r-l
                l = r
                take = dfs(l, r, se[:], cur_len)

            return take + not_take
        
        return dfs(0, 0, , 0)


