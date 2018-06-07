class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSameTree(self, p, q):
		if not q and not p:
			return True
		elif not por not q:
			return False
		elif p.val != q.val:
			return False
		else:
			return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)