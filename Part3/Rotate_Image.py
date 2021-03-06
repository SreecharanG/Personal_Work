class Solution(object):
	def rotate(self, matrix):
		n = len(matrix)
		for row in range(n):
			for column in range(n - row):
				matrix[row][column], matrix[n - 1 - column][n - 1 - row] = matrix[n - 1 - column][n - 1 - row], matrix[row][column]
		for row in range(n // 2):
			for column in range(n):
				matrix[row][column], matrix[n - 1 - row][column] = matrix[n - 1 - row][column], matrix[row][column]
		return matrix