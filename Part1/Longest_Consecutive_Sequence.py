class Solution(object):
	def longestConsecutive(self, nums):
		numset, maxlen = set(nums), 0
		for n in set(nums):
			currlen, tmp = 1, n + 1
			while tmp in numset:
				currlen += 1
				numset.discard(tmp)
				tmp += 1
			tmp = n - 1
			while tmp in numset:
				currlen += 1
				numset.discard(tmp)
				tmp -= 1
			maxlen = max(maxlen, currlen)
		return maxlen
		