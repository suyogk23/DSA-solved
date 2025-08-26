class Solution:
    # solution by @suyogk23 GITHUB
    # use binary search the fine the smallest potion[j] that is >= success when multiplies with spells[i]
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        ans = []
        
        potions.sort()
        for i in range(n):
            l, r = 0, m-1
            while(l < r):
                mid = (l+r)//2
                if spells[i]*potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1
            # r is the idx in portion where the lest potion * spell is >= success
            if spells[i]*potions[r] >= success:
                ans.append(m-r)
            else:
                ans.append(0)
                
        return ans


