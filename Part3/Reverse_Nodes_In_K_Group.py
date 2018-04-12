class ListNode(object):
	self.val = x
	self.next = None

class Solution(object):
	def reverseKGroup(self, head, k):
		if not head or k <= 1:
			return head
		dummy = ListNode(-1)
		dummy.next = head
		temp = dummy
		while temp:
			temp = self.reverseNextK(temp, k)
		return dummy.next

	def reverseNextK(self, head, k):
		temp = head
		for i in range(k):
			if not temp.next:
				return None
			temp = temp.next

		node = head.next
		prev = head
		curr = head.next

		for i in range(k):
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode

		node.next = curr
		head.next = prev
		return node
