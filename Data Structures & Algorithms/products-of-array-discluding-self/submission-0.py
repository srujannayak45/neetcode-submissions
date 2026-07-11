class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        answer=[1]*n

        product=1
        for i in range(n):
            prefix[i]=product
            product*=nums[i]

        product=1
        for i in range(n-1,-1,-1):
            suffix[i]=product
            product*=nums[i]

        for i in range(n):
            answer[i]=prefix[i]*suffix[i]

        return answer
        