class Solution(object):
	def isMatch(self, s, p):
		p_index, s_index, last_s_index, last_p_index = 0, 0, -1, -1
		while s_index < len(s):
			if p_index < len(p) and (s[s_index] == p[p_index] or p[p_index] == '?'):
				s_index += 1
				p_index += 1
			elif p_index < len(p) and p[p_index] == '*':
				p_index += 1
				last_s_index = s_index
				last_p_index = p_index
			elif last_p_index != -1:
				last_s_index += 1
				s_index = last_s_index
				p_index = last_p_index

			else:
				return False
		while p_index < len(p) and p[p_index] == '*':
			p_index += 1

		return p_index == len(p)
		