class Solution(object):
	def reorderList(self, head):
		if not head:
			return

		fast = slow = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			head1, head2 = head, slow.next
			slow.next = None

			cur, pre = head2, None

			while cur:
				nex = cue.next
				cur.next = pre
				pre = cur
				cur = nex

			while cur2:
				nex1, nex2 = cur1.next, cur2.next
				cur1.next = cur2
				cur2.next = nex1
				cur1, cur2 = nex1, nex2
				