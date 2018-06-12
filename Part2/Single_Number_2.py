class Solution(object):
	def singleNumber(self, nums):
		one, two, three = 0, 0, 0
		for num in nums:
			three = two & num
			two = two | one & num
			one = one | num


			one = one & ~three
			two = two & ~three

		return one

	def singleNumber_normal(self, nums):
		result = 0
		for i in range(32):
			count = 0
			for num in nums:
				count += (num >> i) & 1
			rem = count % 3
			if i == 31 and rem:
				result -= 1 <<31
			else:
				resul t |= rem << i
		return result
		