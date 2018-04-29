class Node(object):
	def __init__(self, key, value):
		self.key = key
		self.val = value
		self.prev, self.next = None, None

def __init__(self, capacity):
	self.capacity, self.size = capacity, 0
	self.dic = {}
	self.head, self.tail = self.Node(-1, -1), self.Node(-1, -1)
	self.head.next, self.tail.prev = self.tail, self.head

def _remove(self, node):
	node.prev.next = node.next
	node.next.prev = node.prev
	node.prev, node.next = None, None

def _insert(selfm node):
	node.prev, node.next = self.head, self.head.next
	self.head.next.prev = node
	self.head.next = node

def get(self, key):
	if key not in self.dic:
		return -1
	node = self.dic[key]
	self._remove(node)
	self._insert(node)
	return node.value

def put(self, key, value):
	if key in self.dic:
		node = self.dic[key]
		self._remove(node)
		node.value = value
		self._insert(node)

	else:
		if self.size == self.capacity:
			discard = self.tail.prev
			self._remove(discard)
			del self.dic[discard.key]
			self.size -= 1
		node = self.Node(key, value)
		self.dic[key] = node
		self._insert(node)
		self.size += 1

