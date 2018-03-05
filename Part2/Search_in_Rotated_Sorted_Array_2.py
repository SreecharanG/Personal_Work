class Solution(object):
	def search(self, nums, target):
		left = 0
		right = len(nums) - 1
		while left <= right:
			mid = left + (right - left) // 2
			if nums[mid] == target:
				return True
			if nums[mid] > target:
				if nums[left] <= target pr nums[mid] < nums[left]:
					right = mid - 1
				else:
					left = mid + 1
			else:
				if nums[left] > target or nums[mid] >= nums[left]:
					left = mid + 1
				else:
					right = mid - 1
		return False
		