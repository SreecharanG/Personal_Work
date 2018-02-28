class Solution(object):
	def grayCode(self, n):
		result = [(i >> 1) ^ i for i in range(pow(2, n))]
		return result
		