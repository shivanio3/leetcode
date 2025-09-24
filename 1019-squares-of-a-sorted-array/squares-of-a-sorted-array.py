class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        left,right=0,n-1
        position=n-1
        while left<=right:
            left_square=nums[left]*nums[left]
            right_square=nums[right]*nums[right]
            if left_square>right_square:
                res[position]=left_square
                left+=1
            else:
                res[position]=right_square
                right-=1
            position-=1
        return res
        