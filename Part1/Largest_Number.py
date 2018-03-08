from functools import cmp_to_key

class Solution:
	def largstNumber(sel, nums):
		sorted_nums = sorted(map(str, nums), key = cmp_to_key(lambda x, y:int(y + x) - int(x + y)))
		result = "".join(sorted_nums).lstrip('0')
		return result or '0'
		