class Solution(object):
	def maxArea(self, height):
		if not height:
			return 0
		left = 0
		right = len(height) - 1
		result = 0
		while left < right:
			if height[left] < height[right]:
				area = height[left] * (right - left)
				result = max(result, area)
				left += 1
			else:
				area = height[right] * (right - left)
				result = max(result, area)
				right -= 1

		return result
		
