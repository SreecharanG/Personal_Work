class Solution(object):
	def numDistinct(self, s, t):
		m = len(s)
		n = len(t)
		dp = [0 for __ in range(n + 1)]
		dp[0] = 1
		for i in range(m):
			for j in range(n - 1, -1, -1):
				if t[j] == s[i]:
					dp[j + 1] += dp[j]
		return dp[-1]