class Solution(object):
	def sortColors(self, nums):
		left = mid = 0
		right = len(nums) - 1
		while mid <= right:
			if nums[mid] == 0:
				nums[mid], nums[left] = nums[left], nums[mid]
				left += 1
				mid += 1
			elif nums[mid] == 1:
				mid += 1
			else:
				nums[mid], nums[right] = nums[right], nums[mid]
				right -= 1
				