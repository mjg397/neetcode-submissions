class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # first check if its in dictionary if not put it in
        # if it is in dictionary, return true, if none are
        # then return false if 

        return (len(set(nums)) != len(nums))
        #nums = {}

        #for num in nums:
        #    if nums[num] == 1:
        #        return True
        #    else:
        #        nums[num] = 1;
            
        #return False
        