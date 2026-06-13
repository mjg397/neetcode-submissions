class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        prefix.append(nums[0])
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]*nums[i])
        print(prefix)
        
        suffix = [1] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i]*suffix[i+1]
        
        print(suffix)   

        output = []
        for i in range(len(nums)):
            left = prefix[i-1] if i > 0 else 1
            right = suffix[i+1] if i < len(nums)-1 else 1
            output.append(left * right)
        
        return output
        
       #output = [] 
       #for i in range(len(nums)):
       #     out_prod = 1
       #     for j in range(len(nums)):
       #         if i != j:
       #             out_prod *= nums[j]
       #         
       #     output.append(int(out_prod))

       # return output