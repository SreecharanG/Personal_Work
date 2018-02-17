class(Solution):
	def longestPalindrome2(self, s):
		if not s:
			return
		n = len(s)
		if n == 1:
			return s
		l = r = m = c = 0
		b = True
		for i in range(0, n):
			for j in range(0, min(n - i, i + 1)):
				if (s[i - j] != s[i + j]):
					b = False
					break
				else:
					c = 2 * j + 1
			if (c > m):
				l = i - + 1 - b
				r = i + j + b
				m = c
				b = True

				for j in range(0, min(n - i - 1, i + 1)):
					if(s[i - j] != s[i + j + 1]):
						b = False
						break
					else:
						c = 2 * j + 2

				if (c > m):
					l = i - j + 1 - b
					r = i + 1 + b
					m = c
				b = True
			return s[l:r]
		def longestPalindrome(self, s):
			string = "#" + "#".join(s) + "#"
			i = 0
			maxBorder = 0
			maxCenter = 0
			p = [0 for __ in range(len(string))]
			res = [0, 0]

			while i < len(string):
				p[i] = min(p[2 * maxCenter - i], maxBorder - i) if maxBorder > i else 1
				while i - p[i] >= 0 and i + p[i] < len(string) and string[i - p[i]] == string[i + p[i]]:
					p[i] += 1
				if maxBorder < p[i] + i:
					maxBorder = p[i] + i
					maxCenter = i
					if maxBorder - maxCenter > res[1] - res[0]:
						res = [maxCenter, maxBorder]
				i += 1
			return "".join([x for x in string[2 * res[0] - res[1] + 1 : res[1]] if x != '#'])
 
