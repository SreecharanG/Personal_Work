class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.node1 = None
		self.node2 = None
		self.pre = None


	def recoverTree(self, root):
		self._scan(root)
		self.node1.val, self.node2.val = self.node2.val, self.node1.val


	def _scan(self, root):
		if root is None:
			return
		self._scan(root.left)
		if self.pre is not None:
			if root.val < self.pre.val:
				if self.node1 is None:
					self.node1 = self.pre
					self.node2 = root
				else:
					self.node2 = root
		self.pre = root
		self._scan(root.right)
		