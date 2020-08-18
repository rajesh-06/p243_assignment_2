A=[2, 3.4, 5]
B=[-6, 2, 4]

print('A = ',A)
print('B = ', B)

#Summation of two vector
C=[1,1,1]
for i in range(0,3,1):
	C[i]=A[i]+B[i]
print('A+B = ', C)

#Dot product
dot = 0
for j in range(0,3,1):
	dot += A[j]*B[j]
print('A.B = ',dot)


#output
#A =  [2, 3.4, 5]
#B =  [-6, 2, 4]
#A+B =  [-4, 5.4, 9]
#A.B =  14.8

#[Program finished]


