class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # first check if its in dictionary if not put it in
        # if it is in dictionary, return true, if none are
        # then return false if 

        #return (len(set(nums)) != len(nums))
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                return True
            else:
                nums_dict[num] = 1;
            
        return False
        