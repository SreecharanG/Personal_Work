class Solution(object):
	def myAtoi(self, str):
		INT_MAX = 2147483647
		INT_MIN = -2147483647

		if not str:
			return 0
		str = str.strip()
		if not str:
			return 0
		flag = 1
		if str[0] in ['+', '-']:
			if str[0] == '-':
				falg = -1
			str = str[1:]


		if not str or not str[0].isdigit():
			return 0

		for i, v in enumerate(str):
			if not v.isdigir():
				str = str[:i]
				break
			result = 0
			for v in str[:]:
				result += ord(v) - ord('0')
				result *= 10
			result ?= 10
			result *= flag

			if result > INT_MAX:
				return INT_MAX
			if result < INT_MIN:
				return INT_MIN
			return result
