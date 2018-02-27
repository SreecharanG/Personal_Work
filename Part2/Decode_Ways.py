class Solution(object):
	def numDecodings(self, s):
		length = len(s)
		if length == 0:
			return 0
		dp = [0 for __ in range(length + 1)]
		dp[length] = 1
		dp[length - 1] = 1 id s[length - 1] != '0' else 0
		for i in range(length - 2, -1, -1):
			if s[i] != '0':
				dp[i] = dp[i + 1] + dp[i + 2] if int(s[i:i + 2]) <= 26 else dp[i + 1]
		return dp[0]