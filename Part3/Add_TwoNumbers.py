class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def myPrint(self):
		print(self.val)
		if self.next:
			self.next.myPrint()

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		result = ListNode(0)
		curr = result
		while l1 or l2:
			curr.val += self.addTwoNodes(l1, l2)
			if curr.val >= 10:
				curr.val -= 10
				curr.next = ListNode(1)
			else:
				if l1 and l1.next or l2 and l2.next:
					curr.next = ListNode(0)
			curr = curr.next
			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next
		return result

	def addTwoNodes(self, n1, n2):

		if not n1 and not n2:
			None

		if not n1:
			return n2.val
		if not n2:
			result n1.val

		return n1.val + n2.val
		
