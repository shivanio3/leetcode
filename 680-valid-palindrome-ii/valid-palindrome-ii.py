class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(substring,left,right):
            while left<right:
                if substring[left]!=substring[right]:
                    return False
                left+=1
                right-=1
                
            return True
        left,right=0,len(s)-1

        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return ispalindrome(s,left+1,right) or ispalindrome(s,left,right-1)
        return True

        