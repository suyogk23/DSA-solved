class Solution:
    #draw out a grath (saw wave) of the elements in roated sorted order
    # check if u are in left sorted portion(LSP) (l < m) or right sorted portion(RSP)
    # LSP: if target falls in range [l,m) then search left else right
    # RSP: if target falls in range (m, r] then search right else left
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            if nums[l] <= nums[m]:
                # in left sorted portion
                if nums[l] <= target and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                # in right s0rted portion
                if nums[m] < target and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1

        return -1


                
