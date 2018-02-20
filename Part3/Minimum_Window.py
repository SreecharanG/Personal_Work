from collections import defaultdict

class Solution(object):
	def minWindow(self, s, t):
		MAX_INT = 2147483647
		start = end = 0
		char_need = defaultdict(int)

		count_need = len(t)
		min_length = MAX_INT
		min_start = 0

		for i in t:
			char_need[i] += 1

		while end < len(s):
			if char_need[s[end]] > 0:
				count_need -= 1
			char_need[s[end]] -= 1
			end += 1
			while count_need == 0:
				if min_length > end - start:
					min_length = end -start
					min_start = start
				char_need[s[start]] += 1

				if char_need[s[start]] > 0:
					count_need += 1
				start += 1
		return "" if min_length == MAX_INT else s[min_start:min_start + min_length]