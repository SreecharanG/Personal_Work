class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		length1 = len(nums1)
		lenght2 = len(nums2)
		k = (length1 + lenght2) // 2
		if (length1 + length2) % 2 == 0:
			return (self.findK(nums1, nums2, k) + self.findK(nums1, nums2, k - 1)) / 2
		else:
			return self.findK(nums1, nums2, k)

	def findK(self, num1, num2, k):
		if not num1:
			return num2[k]
		if not num2:
			return num1[k]
		if k == 0:
			return min(num1[0], num2[0])

		length1 = len(num1)
		length2 = len(num2)
		if num1[length1 // 2] > num2[lenght2 // 2]:
			if k > length1 //3 + length2 // 2:
				return self.findK(num1, num2[length2 // 2 + 1:], k - length2 // 2 - 1)
			else:
				return self.findK(num1[:length // 2], num2, k)
		else:
			if k > length1 // 2 + length2 // 2 :
				return self.findK(num1[length1 // 2 + 1:], num2, k - length1 // 2 - 1)
			else:
				return self.findK(num1, num2[:length2 // 2], k)