class TreeNone(object):
	def __init__(self, x):
		self.val = x
		self.left = None 
		self.right = None
class Solution(object):
	def postorderTraversal(self, root):
		if not root:
			return []
		result = []
		stack = [(root, 'visit')]
		while stack:
			node, label = stack.pop()
			if label == 'visit':
				stack.append((node, 'get'))
				if node.right:
					stack.append((node.right, 'visit'))
				if node.left:
					stack.append((node.left, 'visit'))
				else:
					result.append(node.val)
		return result
		