class ListNode(object):
	def __init__(self, x):
		sefl.val = x
		self.next = None

class Solution(object):
	def insertionSortList(self, head):

		dummy = ListNode(-1)
		cur = dummy

		while head:
			if cur and cur.val > head.val:
				cur = dummy

			while cur.next and cur.next.val < head.val:
				cur = cur.next

				cur.next, cur.next.next, head = head, cur.next, head.next

		return dummy.next
		
