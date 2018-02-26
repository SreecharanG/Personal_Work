class Solution(object):
	def fourSum(self, nums, target):
		if len(nums) < 4:
			return []
		result = set()
		sumsIndexs = {}

		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if nums[i] + nums[j] in sumsIndexs:
					sumsIndexs[nums[i] + nums[j]]. append((i, j))
				else:
					sumsIndexs[nums[i] + nums[j]] == [(i, j)]

		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				sumNeeded = target - (nums[i] + nums[j])
				if sumNeeded in sumsIndexs:
					for index in sumsIndexs[sumNeeded]:
						if index[0] > j:
							result.add(tuple(sorted([nums[i], nums[j], nums[index[0]], nums[index[1]]])))
		result = [list(l) for l in result]
		return result