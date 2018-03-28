class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
		def mu_print(self):
			print(self.val)
			if self.next:
				print(self.next.val)


class Solution(object):
	def deleteDuplicates(self, head):
		dummy = ListNode(-1)
		dummy.next = head
		curr = dummy
		is_repeat = False
		while curr.next:
			while curr.next.next and curr.next.val == curr.next.next.next.val:
				curr.next = curr.next.next
				is_repeat = True
			if is_repeat:
				curr.next = curr.next.next
				is_repeat = False
			else:
				curr = curr.next
		return dummy.next
		