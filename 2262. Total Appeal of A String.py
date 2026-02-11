class Solution:
    def appealSum(self, s: str) -> int:
        s = _+s # to get 1 indexed string
        hm = defaultdict(int)
        ans = 0

        for i, c in enumerate(s):
            if i > 0:
                hm[c] = i
                ans += sum(hm.values())

        return ans
        # in 1 indexed array, the num of prev substr ending with current char == idx
        # sum(hm.values()):
        # (after processing 'a', 'b', 'b')
        # hm = {a:1, b:3}
        # Substrings ending at position 2:
        # b [2,2]: contains 'b' → appeal = 1
        # bb [1,2]: contains 'b' → appeal = 1
        # abb [0,2]: contains 'a' and 'b' → appeal = 2
        # total appeal = 4
        # also until we reached ('a', 'b', 'b'), we already calculated appeal for subarray from right to left
        # ('a', 'b')
        # b = 1
        # ab = 2
        # ('a')
        # a = 1
        # hence if we total all these we get 8
        
