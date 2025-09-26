class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mp=0
        bb=prices[0]
        for i in range(1,n):
            mp=max(mp,prices[i]-bb)
            bb=min(bb,prices[i])
        return mp
        