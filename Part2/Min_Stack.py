class MinStack(object):
	def __init__(self):
		self.stack = []
		self.minStack = []

	def push(self, x):
		self.stack.append(x)
		if not self.minStack:
			self.minStack.append(x)
		else:
			if self.minStack[-1] >= x:
				self.minStack.append(x)

	def pop(self):
		if self.stack:
			if self.minStack[-1] == self.stack[-1]:
				self.minStack.pop()
			self.stack.pop()

	def top(self):
		if self.stack:
			return self.stack[-1]

	def getMin(self):
		if self.minStack:
			return self.minStack[-1]
			
