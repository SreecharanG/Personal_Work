# Printing all the numbers

a_2d = [[1,2,3],[5,6,7]]
print (a_2d)

# To replace the element

b_2d = [[1,2,3],[5,6,7]]
b_2d[1][1] = 99
print (b_2d)

#Iterate Over c_2d And Print all the syntax

c_2d = [[1,2,3],[5,6,7]]
for i in c_2d:
	for item in i:
		print(item)

#Print all the numbers using range of
d_2d = [[1,2,3],[5,6,7]]
for i in range(d_2d):
	for j in range(d_2d[i]):
		print(d_2d[i][j])

#Adding the numbers in diagnoal
def diagnoal_sum():
	given2_d = [[1,2,3],[4,5,6],[7,8,9]]
	total = 0
	for i in range (len(given2_d):
		total += given2_d[i][i]
	return (total)


#Sample Interview Question
#Chess Board any of the rookies can able to attack any one horizantally and Vertically
def rook_safe(chessboard):
	n = len(chessboard)
	
	for row_i in range(n):
		row_count =0
		for col_i in range(n):
			row_count +=chessboard[row_i][col_i]
		if row_count > 1:
			return False

	for col_i in range(n):
		col_count =0
		for col_i in range(n):
			col_count +=chessboard[row_i][col_i]
		if col_count>1:
			return False

	return True

