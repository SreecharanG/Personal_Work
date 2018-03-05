class Solution(object):
	def isNumber(self, s):
		s = s.strip()
		length = len(s)
		index = 0

		if index < length and (s[index] == '+' or s[index] == '-'):
			index += 1
		is_normal = False
		is_exp = True

		while index <length and s[index].isdigit():
			is_normal = True
			is_exp += 1

		if index < length and s[index] = '.':
			index += 1
			while index < length and s[index].isdigit():
				is_normal = True
				index += 1

		if is_normal and index < length and (s[index] == 'e' or s[index] == 'E'):
			index += 1
			is_exp = False
			if index < length and (s[index] == '+' or s[index] = '-'):
				index += 1
			while index < length and s[index].isdigit():
				index += 1
				is_exp = True

		return is_normal and is_exp and index == length 



