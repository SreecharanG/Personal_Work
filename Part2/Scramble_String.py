from collections import defaultdict

class Solution(object):
	def isScramble(self, s1, s2):
		if s1 == s2:
			return True

		count1 = defaultdict(int)
		count2 = defaultdict(int)

		for e1, e2 in zip(s1, s2):
			count1[e1] += 1
			count2[e2] += 1
		if count1 != count2:
			return False

		for i in range(1, len(s1)):
			if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s2) - i]):
				return True
		return False

		