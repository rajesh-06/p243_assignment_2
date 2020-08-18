#To get the distance between 2 points
def distance(x1, x2, y1, y2):
	if((x2-x1)>=0 and (y2-y1)>=0):
		return ((x2-x1)+(y2-y1))
	elif((x2-x1)<=0 and (y2-y1)>=0):
		return ((x1-x2)+(y2-y1))
	elif((x2-x1)<=0 and (y2-y1)<=0):
		return ((x1-x2)+(y1-y2))
	elif((x2-x1)>=0 and (y2-y1)<=0):
		return ((x2-x1)+(y1-y2))
		
sum=0
n=0

print("To find the average distance between 2 points on a M by N two dimensional grid(no diagonal connection).")
#Number of points in a column
y= input ('Enter the number of points in a column: ')
#number of points in a row
x= input ('Enter the number of points in row: ')

try:
	r = int(y)
	c = int(x)
	#Summing all the possible distances
	if (r>=0 and c>=0):
		for X1 in range(c):
			for X2 in range(c):
				for Y1 in range(r):
					for Y2 in range(r):
						sum+=distance(X1,X2,Y1,Y2)
						n+=1
		print('The average distance between 2 points in the grid is:',sum/n)		
	else:
		print('It is not possible to form a grid with the entered value.')
		
except ValueError:
	print('It is not possible to form a grid with the entered value.')
	
#Output
#To find the average distance between 2 points on a M by N two dimensional grid(no diagonal connection).
#Enter the number of points in a column: 6
#Enter the number of points in row: 6
#The average distance between 2 points in the grid is: 3.888888888888889

#[Program finished]