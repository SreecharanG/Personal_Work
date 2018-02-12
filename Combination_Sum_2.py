class Solution(object):
	def combinationSum2(self, candidates, target):
		if not candidates:
			return []
		candidates.sort()
		result = []
		self.combination(candidates, target, [], result)
		return result

	def combination(self, candidates, target, current, result):
		s = sum(current) if current else 0
		if s > target:
			return
		elif s == target:
			result.append(current)
			return
		else:
			i = 0
			while i < len(candidates):
				self.combination(candidates[i + 1:], target. current + [candidates[i]], result)
				while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
					i += 1
				i += 1
