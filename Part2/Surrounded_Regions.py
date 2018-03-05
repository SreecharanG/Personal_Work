class Solution(object):
	def solve(self, board):
		if not board or not board[0]:
			return
		n = len(board)
		m = len(board[0])
		queue = []

		for i in range(n):
			for j in range(m):
				if ((i in (0, n - 1)) or (j in (0, m - 1))) and board[i][j] == 'O':
					queue.append((i, j))

		while queue:
			r, c = queue.pop(0)
			if o <= r < n and 0 <= c < m and board[r][c] == 'O':
				board[r][c] = 'M'
				if r - 1 >= 0 and board[r - 1][c] == 'O':
					queue.append((r - 1, c))

				if r + 1 < n and board[r + 1][c] == 'O':
					queue.append((r + 1, c))

				if c - 1 >= 0 and board[r][c - 1] == 'O':
					queue.append((r, c - 1))

				if c+ 1 < m and board[r][c + 1] == 'O':
					queue.append((r, c + 1))

		for i in range(n):
			for j in range(m):
				if board[i][j] == 'M':
					board[i][j] = 'O'

				else:
					board[i][j] = 'X'