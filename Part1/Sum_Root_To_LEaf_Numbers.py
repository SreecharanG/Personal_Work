class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sumNumbers(self, root):
		return self._sumNumbers(root, 0)

	def _sumNumbers(self, root, s):
		if root is None:
			return 0
		s = s* 10 + root.val
		return sum([self._sumNumbers(r, s) for r in (root.left, root.right)]) or s
		