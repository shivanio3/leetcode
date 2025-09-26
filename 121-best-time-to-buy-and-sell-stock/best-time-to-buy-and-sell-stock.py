class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        mp=0
        bb=prices[0]
        for i in prices:
            mp=max(mp,i-bb)
            bb=min(bb,i)
        return mp
        