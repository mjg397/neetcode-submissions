class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I must store the target-number in a hash map and then check
        # for hits of the hash map.

        hash_map = {} 

        for i in range(len(nums)):
            num = nums[i]
            value = target - num
            if not(value in hash_map):
                hash_map[num] = i
                print(hash_map)
            else:
                return[hash_map[value], i]


