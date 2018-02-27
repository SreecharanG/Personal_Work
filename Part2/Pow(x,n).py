class Solution(object):
	def myPow(self, x, n):
		flag = 1if n >= 0 else -1
		result = 1
		n = abs(n)
		while n > 0:
			if n & 1 == 1:
				result *= x
			n >>= 1
			x *= x
		if flag < 0:
			result = 1 / result
		return result
		