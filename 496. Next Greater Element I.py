class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # TC: O(m * n)
        # scan right to left
        # maintain a monotonic stack that stores element in decreasing order only
        # that is if current element is smaller than top, only then pus to stack else pop
        hm = {}
        monostk = []
        for n in nums2[::-1]:
            while monostk and n >= monostk[-1]:
                monostk.pop()
            if not monostk:
                hm[n] = -1
            else:
                hm[n] = monostk[-1]
            monostk.append(n)

        ans = []
        for n in nums1:
            ans.append(hm[n])
        return ans
