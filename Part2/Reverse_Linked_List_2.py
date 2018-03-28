class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def to_list(self):
		return [self.val] + self.next.to_list() if self.next else [self.val]

class Solution(object):
	def reverseBetween(self, head, m, n):
		dummy = ListNode(-1)
		dummy.next = head
		node = dummy
		for __ in range(m - 1):
			node = node.next

		prev = node.next
		curr = prev.next
		for __ in range(n - m):
			next = curr.next
			curr.next = prev
			prev = curr
			curr = next
		node.next.next = curr
		node.next = prev
		return dummy.next
		