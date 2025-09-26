class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        cs=0
        ms=float('-inf')
        for i in range(n):
            cs=cs+nums[i]
            ms=max(cs,ms)
            if cs<0:
                cs=0
        return ms
        