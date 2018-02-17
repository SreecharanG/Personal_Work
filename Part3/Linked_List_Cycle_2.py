class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def detextCycle(self, head):
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				node = head
				while node != slow:
					node = node.next
					slow = slow.next
				return node 
		return None
		