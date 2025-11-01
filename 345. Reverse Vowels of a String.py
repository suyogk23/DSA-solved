class Solution:
    def reverseVowels(self, s: str) -> str:
        # solution by @suyogk23 GITHUB
        # linear 2 ptr swap approach
        # left and right ptr to track vow, if both are vow then swap
        n = len(s)
        s_arr = list(s)
        l, r = 0, n-1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        while (l<n and r>=0 and l<r):
            if s_arr[l].lower() not in vowels:
                l+=1
            if s_arr[r].lower() not in vowels:
                r-=1
            if s_arr[l].lower() in vowels and s_arr[r].lower() in vowels:
                #swap
                s_arr[l], s_arr[r] = s_arr[r], s_arr[l]
                l+=1
                r-=1
        return "".join(s_arr)

