class Solution(object):
	def rotate(self, nums, k):

		def reverse(nums,start, end):
			while start <end:
				nums[start], nums[end] = nums[end], nums[start]
				start += 1
				end -= 1

		n = len(nums)
		k %= n
		reverse(nums, 0, n - k - 1)
		reverse(nums, n - k, n - 1)
		reverse(nums, 0, n - 1)