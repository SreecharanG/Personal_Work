class Solution(object):
	def numTrees(self, n):
		dp = [1 for __ in range(n + 1)]
		for i in range(2, n + 1):
			s = 0
			for j in range(i):
				s += dp[j] * dp[i - 1 - j]
			dp[i] = s
		return dp[-1]
		