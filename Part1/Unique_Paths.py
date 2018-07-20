import math
class Solution(object):
	def uniquePaths(self, m, n):
		m -= 1
		n -= 1
		return math.factorial(m + n)/ (math.factorial(n) * math.factorial(m))



class _Solution(object):
	def _uniquePaths(self, m, n):
		dp = [[1 for __ in range(n)] for __ in range(m)] 
		for i in range(1, n):
			doe j in range(1, m):
			dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
		return dp[m - 1][n - 1]