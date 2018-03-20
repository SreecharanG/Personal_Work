class Solution(object):
	def isPalindrome(self, s):
		alphanumerics = [c for c in s.lower() if s.isalnum()]
		return alphanumerics == alphanumerics[::-1]
		