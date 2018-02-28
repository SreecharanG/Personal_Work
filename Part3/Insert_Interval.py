class interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

	def __str__(self):
		return "[" + str(self.start) + "," + str(self.end) + "]"
class Solution(object):
	def insert(self, intervals, newInterval):
		start, end = newInterval.start, newInterval.end
		left = list(filter(lambda x: x.end < start, intervals))
		right = list(filter(lambda x: x.start > end, intervals))
		if len(left) + len(right) != len(intervals):
			start = min(start, intervals[len(left)].start)
			end = max(end, intervals[-len(right) - 1].end)

		return left + [interval(start, end)] + right
		