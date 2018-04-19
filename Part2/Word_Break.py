class Solution(object):
	def wordBreak(self, s, wordDict):
		n = len(s)
		dp = [False] * (n + 1)
		dp[0] = True

		for i in range(n):
			for j in range(i, -1, -1):
				if dp[j] and s[j:i + 1] in wordDict:
					dp[i + 1] = True
					break
		return dp[n]


		