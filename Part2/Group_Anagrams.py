class Solution(object):
	def groupAnagrams(self, strs):
		maps = {}
		for i, v in enumerate(strs):
			target = "".join(sorted(v))
			if target not in map:
				map[target] = [v]
			else:
				map[target].append(v)
		result = []
		for value in map.values():
			result += [sorted(value)]
		return result