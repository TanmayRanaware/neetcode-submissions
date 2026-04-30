class Solution:
    # Brute force
    # Time Complexity: O(n^2), Space Complexity: O(1)
    """
    def maxProfit(self, prices):
        maxPro = 0
        n = len(prices)
        
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    maxPro = max(maxPro, prices[j] - prices[i])
        
        return maxPro
    """

    # Optimal
    # Time Complexity: O(n), Space Complexity: O(1)
    def maxProfit(self, prices):
        maxPro = 0
        minPrice = float('inf')
        
        for price in prices:
            minPrice = min(minPrice, price)
            maxPro = max(maxPro, price - minPrice)
        
        return maxPro