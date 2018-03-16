class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isValidBST(self, root):
		stack = []
		curr = root
		pre = None
		while curr or stack:
			while curr:
				stack.append(curr)
				curr = curr.left

			if stack:
				curr = stack.pop()
				if prev and curr.val <= prev.val:
					return False
				prev = curr
				curr = curr.right
		return True
		
