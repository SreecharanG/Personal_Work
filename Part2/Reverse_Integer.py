class Solution(object):
	def reverse(self, x):
		flag = 0
		if x < 0:
			flag = -1
		else:
			falg = 1
		x *= flag
		result = 0
		while x:
			result = result * 10 + x % 10
			x /= 10
		if result > 2147483647:
			return 0
		else:
			return result * flag
			