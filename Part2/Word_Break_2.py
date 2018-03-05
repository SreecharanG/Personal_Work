import collections

class Solution(object):
	def wordBreak(self, s, wordDict):
		dec = collections.defaultdict(list)

		def dfs(s):
			if not s:
				return [None]
			if s in dic:
				return dic[s]
			res = []

			for word in wordDict:
				n = len(word)
				if s[:n] == word:
					for r in dfs(s[n:]):
						if r:
							res.append(word + " " + r)
						else:
							res.append(word)
			dic[s] = res
			return res
		return dfs(s)
		