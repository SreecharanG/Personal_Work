class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def pathSum(self, root, sum):
		result = []
		self._pathSum(root, sum, [], result)
		return result

	def _pathSum(self, root, sum, curr, result):
		if not root:
			return
		sum -= root.val
		if sum == 0 and root.left is None and root.right is None :
			result.append(curr + [root.val])

		if root.left:
			self._pathSum(root.left, sum, curr + [root.val], result)
		if root.right:
			self._pathSum(root.right, sum, curr + [root.val], result)