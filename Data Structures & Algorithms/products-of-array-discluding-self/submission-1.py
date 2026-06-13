class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums)):
            out_prod = 1
            for j in range(len(nums)):
                if i != j:
                    out_prod *= nums[j]
                
            output.append(int(out_prod))

        return output