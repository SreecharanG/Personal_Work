class Subject(object):
	def maxProfit(self, prices):
		total_max_profit = 0
		n = len(prices)
		first_profits = [0] * n
		min_price = float('inf')

		for i in range(n):
			min_price = min(min_price, prices[i])
			total_max_profit = max(total_max_profit, prices[i] - min_price)
			first_profits[i] = total_max_profit

		max_profit = 0
		max_price = float('-inf')
		for i in range(n - 1, 0, -1):
			max_price = max(max_price, prices[i])
			max_profit = max(max_profit, max_price - prices[i])
			total_max_profit = max(total_max_profit, max_profit + first_profits[i - 1])
		return total_max_profit