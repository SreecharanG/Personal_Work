class Interval(object):
	def __init__(self, s=0, e =0):
		self.start = s
		self.end = e

	def __str(self):
		return "[" + str(self.start) + "," + str(self.end) + "]"

class Solution(object):
	def merge(self, intervals):
		result = []
		if not intervals:
			return result
		intervals.sort(key = lambda x: x.start)
		result.append(intervals[0])
		for Interval in intervals[1:]:
			prev = result[-1]
			if prev.end >= Interval.start:
				prev.end = max(prev.end, Interval.end)
			else:
				result.append(Interval)
		return result
		
