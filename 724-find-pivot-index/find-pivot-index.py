class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left_sum=0
        total=sum(nums)
        for i in range(len(nums)):
            right_sum=total-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1
        