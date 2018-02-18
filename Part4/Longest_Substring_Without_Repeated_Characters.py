class Solution(object):
	def lengthofLongestSubstring(self, s):
		if not s:
			return 0
		if len(s) <= 1:
			return len(s)

		locations - [ -1 for i in range(256)]
		index = -1
		m = 0
		for i, v in enumerate(s):
			if (locations[ord(v)] > index):
				index = locations[ord(v)]

			m = max(m, i - index)
			location[ord(v)] = i
		return m