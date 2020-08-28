"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Problem
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Strategy : 3 types of state [buy, sell, cooldown] -> 2 types of state [hold, unhold]

- Hold : At the end of today, the maximum profit if you hold stock
- Unhold : At the end of today, the maximum profit if you unhold stock

We have the following ways to enter each state:

Hold:
	1) you bought the stock today -> Hold
	2) you did not sell the stock that you bought before -> Hold

Unhold
	1) you sold the stock today
	2) you did not buy any stock after you sold last stock
	
Then, the answer should be when you not hold stock, the maximum profit.

# 1   : First day & Hold == you bought the stock with price prices[0], then your profit should be -prices[0]
# 2-1 : ith hold   <- 1) you buy stock today == you sold the stock before and you should task cool down before buy the stock
				      2) you bought stock before and just not sell it today
				      
# 2-2 : ith unhold <- 1) you sell out the stock today (hold->sell)
                      2) you sold out the stock before and do nothing (sell->cooldown)

"""


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		N = len(prices)
		if N<2:
			return 0
		
		hold = [0] * N # ith day profit when you hold stock
		unhold = [0] * N # ith day profit when you unhold stock
		
		# 1
		hold[0] = -prices[0]
		for i in range(1,N):
			
			hold[i] = max(unhold[i-2]-prices[i], hold[i-1]) # 2-1
			unhold[i] = max(hold[i-1]+prices[i], unhold[i-1]) # 2-2
		return unhold[N-1]
