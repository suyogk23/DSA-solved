class Solution:
    # solution by suyogk23
    # keep track of latest index where non zero element can be placed
    # iterate the array with for loop and if non zero element encountered
    # swap the non zero element with latest non zero index
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        latestNonZero = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                #swap 
                nums[latestNonZero], nums[i] = nums[i], nums[latestNonZero]
                latestNonZero += 1
        

        

            
            
