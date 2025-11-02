class Solution:
    # solution by @suyogk23 GITHUB
    # pythonic solution
    # split the str according to whitespace and make it to an array or words
    # reverse the array of words
    # join the words in array on " " (space), then strip() the string (removes leading and trailing spaces)
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words).strip()
