class Solution(object):
	def calculateMinimumHp(self, dungeon):
		n = len(dungeon)
		m = len(dungeon[0])
		dp = [[0 for __ in range(m)] for __ in range(n)]
		dp[-1][-1] = 1 if dungeon[-1][-1] > 0 else 1 - dungeon[-1][-1]

		for i in range(m - 2, -1, -1):
			dp[-1][i] = max(1, dp[-1][i + 1] - dungeon[-1][i])

		for j in range(n - 2, -1, -1):
			dp[j][-1] = max(1, dp[j + 1][-1] - dungeon[j][-1])

		for j in range(n - 2, -1, -1):
			for i in range(m - 2, -1, -1):
				dp[j][i] = max(min(dp[j + 1][i], dp[j][i + 1]) - dungeon[j][i], 1)
		return dp[0][0]