class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxPathSum(self, root):
		self.maxSum = float('-inf')
		self._maxPathSum(root)
		return self.maxSum

	def _maxPathSum(self, root):
		if root is None:
			return 0
		left = self._maxPathSum(root.left)
		right = self._maxPathSum(root.right)
		left = left if left > 0 else 0
		right = right if right > 0 else 0
		self.maxSum = max(self.maxSum, root.val + left + right)
		return max(left, right) + root.val
		