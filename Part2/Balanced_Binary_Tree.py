class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isBalanced(self, root):
		return self._isBalanced(root) >= 0 

	def _isBalanced(self, root):
		if not root:
			return 0
		left, right = self._isBalanced(root.left), self._isBalanced(root.right)
		if left >= 0 and right >= 0 and abs(left - right) <= 1:
			return 1 + max(left, right)

		else:
			return -1

			