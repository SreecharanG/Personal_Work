class Solution(object):
	def totalNQueens(self, n):
		self.com = [False] * n
		self.diag = [False] * (2 * n)
		self.anti_diag = [False] * (2 * n)
		self.result = 0
		self.recursive(0, n)
		return self.result

	def recursive(self, row, n):
		if row == n:
			self.result += 1
		else:
			for i in range(n):
				if not self.col[i] and not self.diag[row + i] and not self.anti_diag[n - i + row]:
					self.col[i] = self.diag[row + i] = self.anti_diag[n - i + row] = True
					self.recursie(row + 1, n)
					self.col[i] = self.diag[row + i] = self.anti_diag[n - i + row] = False
					
