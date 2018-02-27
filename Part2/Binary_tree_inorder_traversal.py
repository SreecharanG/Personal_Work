class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def inOrderTransversal(self, root):
		result = []
		stack = []
		p = root

		while p or stack:
			while p:
				stack.append(p)
				p = p.left
			if stack:
				p = stack.pop()
				result.append(p.val)
				p = p.right
		return result
		