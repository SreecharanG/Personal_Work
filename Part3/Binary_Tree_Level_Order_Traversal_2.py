class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrderBottom(self, root):
		result = []
		if not root:
			return result
		curr_level = [root]
		while curr_level:
			level_result = []
			next_level = []
			for temp in curr_level:
				level_result.append(temp.val)
				if temp.left:
					next_level.append(temp.left)
				if temp.right:
					next_level.append(temp.right)
			result.append(level_result)
			curr_level = next_level
		result.reverse()
		return result