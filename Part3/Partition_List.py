class Solution(object):
	def partition(self, head, x):
		dummy = ListNode(-1)
		dummy.next = head
		small_dummy = ListNode(-1)
		large_dummy = ListNode(-1)


		prev = dummysmall_prev = small_dummy
		large_prev = large_dummy

		while prev.next:
			curr = prev.next
			if curr.val < x:
				small_prev.next = curr
				small_prev = small_prev.next

			else:
				large_prev.next = curr
				large_prev = large_prev.next
			prev = prev.next

		large_prev.next = None
		small_prev.next = large_dummy.next
		return small_dummy.next

		