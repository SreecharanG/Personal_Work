class Solution(object):
	def simplifyPath(self, path):
		parts = path.split("/")
		result = ['']
		for part in parts:
			if part:
				if part not in ('.', '..'):
					if len(result) == 0:
						result.append('')
					result.append(part)
				elif part == '..' and len(result) > 0:
					result.pop()
		if len(result) < 2:
			return "/"
		else:
			return "/".join(result)