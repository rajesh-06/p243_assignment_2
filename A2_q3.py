with open('M.txt', 'r') as f:
    M = [[float(num) for num in line.split(' ')] for line in f]
print('M =', M)

with open('N.txt', 'r') as f:
    N = [[float(num) for num in line.split(' ')] for line in f]
print('N =',N)

A=[2,3,5]
print('A =',A)
p1=[[0,0,0], [0,0,0], [0,0,0]]
p2=[0,0,0]

for i in range(3):
    for x in range(3):
        for j in range(3):
            p1[i][j] = p1[i][j] + (M[i][x] * N[x][j]) 
print("Product of M*N =", p1)

for i in range(3):
	for j in range(3):
		p2[i] = p2[i] + (M[i][j] * A[j])		
print("Product of M*A =",p2)

#Output
#M = [[4.0, -2.0, 5.0], [1.0, 3.0, -6.0], [0.0, -1.0, 7.0]]
#N = [[1.0, 6.0, -2.0], [0.0, 3.0, 4.0], [-6.0, 5.0, 7.0]]
#A = [2, 3, 5]
#Product of M*N = [[-26.0, 43.0, 19.0], [37.0, -15.0, -32.0], [-42.0, 32.0, 45.0]]
#Product of M*A = [27.0, -19.0, 32.0]

#[Program finished]