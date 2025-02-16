class Solution:
	#add list to set, then check if each num is start of seq, 
	#i.e, there must be no num-1 in set
	#then calculate seq len
	#return max len
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_seq = 0

        for i in nums_set:
            #check if start of a seq
            if (i-1) not in nums_set:
                seq = 0
                #check seq length
                while(i+seq) in nums_set:
                    seq+=1
                max_seq = max(max_seq, seq)

        return max_seq
