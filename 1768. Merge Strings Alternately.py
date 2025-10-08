class Solution:
    # soultion by @suyogk23 GITHUB
    # alternatively merge string and merge either remaining strs (like merge function in merge sort)
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        n1, n2 = len(word1), len(word2)
        merged_string = ''
        # alternatively merge strs
        while p1 < n1 and p2 < n2:
            merged_string = merged_string + word1[p1] + word2[p2]
            p1 += 1
            p2 += 1
        # merge remaining strs if any
        if p1 < n1:
            merged_string = merged_string + word1[p1:n1]
        if p2 < n2:
            merged_string = merged_string + word2[p2:n2]
        
        return merged_string
