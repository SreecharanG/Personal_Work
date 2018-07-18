class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def myPrint(self):
		if self.next:
			self.next.myPrint()

class Solution(object):
	def removeNthFromEnd(self, head, n):
		if not head:
			return head
		dummy = ListNode(-1)
		dummy.next = head
		prev = dummy
		cur = dummy
		while prev and n >= 0:
			prev = prev.next
			n -= 1
		while prev:
			prev = prev.next
			cur = cur.next
		cur.next = cur.next.next
		return dummy.next