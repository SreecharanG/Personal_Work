class Solution(object):
	def rotateRight(self, head, k):
		if not head:
			return []
		curr = head
		length = 1
		while curr.next:
			curr = curr.next
			length += 1
		curr.next = head
		cur = head
		shift = length - k % length
		while shift > - :
			curr = curr.next
			shift -= 1
		result = curr.next
		curr.next = None
		return result
		
