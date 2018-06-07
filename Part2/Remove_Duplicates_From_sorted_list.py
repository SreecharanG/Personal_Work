class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

	def my_print(self):
		print(self.val)
		if self.next:
			print(self.next.val)

class Solution(object):
	def deleteDuplicates(self, head):
		curr = head
		while curr:
			while curr.next and curr.val == curr.next.val:
				curr.next = curr.next.next
			curr = xurr.next
		return head

		