class Solution(object):
	def maxSubArray(self, nums):
		if not nums:
			return 0
			length = len(nums)
			current = nums[0]
			m = current
			for i in range(1, length):
				if current < 0:
					current = 0
				current += nums[i]
				m = max(current, m)
			return m