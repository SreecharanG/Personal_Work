class Solution(object):
	def removeDuplicates(self, nums):
		if not nums:
			return 0
		index = 1
		start = 0
		for i in range(1, len(nums)):
			if nums[start] != nums[i]:
				nums[index] = nums[i]
				index += 1
				start = i
		return index
		