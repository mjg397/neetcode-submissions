class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = int(l + (r-l) / 2) # get this correct for overflows

            if (nums[m] == target):
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

