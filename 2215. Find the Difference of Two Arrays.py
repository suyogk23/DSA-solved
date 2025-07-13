class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash_set_1 = set(nums1)
        hash_set_2 = set(nums2)

        ans = []
        ans1 = []
        ans2 = []

        for i in hash_set_1:
            if i not in hash_set_2:
                ans1.append(i)
        
        for i in hash_set_2:
            if i not in hash_set_1:
                ans2.append(i)
        ans.append(ans1)
        ans.append(ans2)
        return ans
