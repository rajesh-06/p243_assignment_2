sum=0
m=0
print("To find the average distance between 2 points on a straight line made up of N discrete points having eqaul interval of 1 unit.")
y = input('Enter the number of points in that chain: ')
try:
	n=int(y)
	if n>=0:
		for i in range(0,n):
			for j in range(0, n):
				if(i>=j):
					sum+=i-j
					m+=1
				else:
					sum+=j-i
					m+=1
		print('The average distance between 2 points is: ', sum/m)		
	else:
		print('The input value is not a whole number')
except ValueError:
	print("It is not possible to create a chain with the entered value. ")

#Output	
#To find the average distance between 2 points on a straight line made up of N discrete points having eqaul interval of 1 unit.
#Enter the number of points in that chain: 6
#The average distance between 2 points is:  1.9444444444444444

#[Program finished]