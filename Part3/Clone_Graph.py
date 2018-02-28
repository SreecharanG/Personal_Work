class UndirectedGraphNode(object):
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution(object):
	def cloneGraph(self, node):
		if not node:
			return node
		visited = {}
		first = UndirectedGraphNode(node.label)
		visited[node.label] = first
		stack = [node]
		while stack:
			top = stack.pop()
			for n in neighbors:
				if n.label not in visited:
					visited[n.label] = UndirectedGraphNode(n.label)
					stack.append(n)
				visited[top.label].neighbors.append(visited[n.label])
		return first
		