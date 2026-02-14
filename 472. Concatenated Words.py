class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Time: O(n * w^3)
        # space: O(n) + O(w); O(n) for set, O(w) for hashmap, O(w) for recursion stack
        # for a word check each and every possible substring from i->j then continue the search until len(word), if we reach end
        # and the last substr in set then the word is valid concatenated word
        words_set = set(words)

        def isValid(word): # O(w^3)
            n = len(word)
            dp = {}
            def dfs(start):
                if start == n:
                    return True
                if start in dp:
                    return dp[start]
                #O(w^2) # w possible start and w possible end points
                for end in range(start+1, n+1): 
                    substr = word[start:end] #O(w)
                    if substr != word and substr in words_set:
                        if dfs(end):
                            dp[end] = True
                            return dp[end]
                dp[start] = False
                return dp[start]
            
            return dfs(0)
        
        concat_words = []

        for word in words:
            if isValid(word): #O(n)
                concat_words.append(word) # O(w^3)
        
        return concat_words



