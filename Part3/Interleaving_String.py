class Solution(object):
	def isInterleave(self, s1, s2, s3):
		m = len(s1)
		n = len(s2)
		l = len(s3)
		if m + n != l:
			return False
		dp = [True for __ in range(m + 1)]
		for i in range(m):
			dp[i + 1] = dp[i] and s1[i] == s3[i]
		for j in range(n):
			dp[0] = dp[0] and s2[j] == s3[j]
			for i in range(m):
				dp[i + 1] = (dp[i] and s1[i] == s3[i + j + 1]) or (dp[i + 1] and s2[j] == s3[i + j + 1])
		return dp[m]
		