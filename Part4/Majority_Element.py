class Solution(object):
	def majorityElement(self, nums):
		result = None
		count = 0
		for num in nums:
			if count == 0:
				result = num
			if result == num:
				count += 1
			else:
				count -= 1
		retirn result
		