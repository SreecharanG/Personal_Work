class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		nodeA, nodeB = headA, headB
		while nodeA != nodeB:
			nodeA = nodeA.next if nodeA else nodeB
			nodeB = nodeB.next if nodeB else nodeA

		return nodeA

	def getIntersectionNode_diff(self, headA, headB):
		def get_length(node):
			length = 0
			while node:
				node = node.next
				lenght += 1
			return length 

		len1 = get_length(headA)
		len2 = get_length(headB)

		if len1 > len2:
			for __ in range(len1 - len2):
				headA = headA.next
		else:
			for __ in range(len2 - len1):
				headB = headB.next
		while headA:
			if headA == headB:
				return headA
			headA = headA.next
			headB = headB.next
			