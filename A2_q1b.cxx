#include<iostream>
using namespace std;

//To get the distance between 2 points.
int distance(int x1, int x2, int y1, int y2){
	if((x2-x1)>=0 && (y2-y1)>=0){
		return ((x2-x1)+(y2-y1));
	}
	else if((x2-x1)<=0 && (y2-y1)>=0){
		return ((x1-x2)+(y2-y1));
	}
	else if((x2-x1)<=0 && (y2-y1)<=0){
		return((x1-x2)+(y1-y2));
	}
	else if((x2-x1)>=0 && (y2-y1)<=0){
		return ((x2-x1)+(y1-y2));
	}
}

//main function
int main()
{
cout<<"To find the average distance between 2 points on a M by N two dimensional grid(no diagonal connection)"<<endl;
int c, r;
int n=0;
cout<<"Enter the number of columns in your grid: ";
cin>>c;
cout<<"Enter the number of rows in your grid: ";
cin>>r;
float sum=0;

//for average 
if(c>=0 && r>=0){
	for(int X1 =0; X1<c; X1++){
		for(int X2=0; X2<c; X2++){
			for(int Y1=0; Y1< r; Y1++){
				for(int Y2=0; Y2< r; Y2++){
					sum+=distance(X1, X2, Y1, Y2);
					n++;
				}
			}
		}
	}
cout<<"The average distance between two points in the grid is: "<< sum/n<<endl;
}

else cout<<"It is not possible to form a 2 dimensional grid with your entered number."<<endl;
				
	return 0;
}

/*
output
To find the average distance between 2 points on a M by N two dimensional grid(no diagonal connection)
Enter the number of columns in your grid: 6
Enter the number of rows in your grid: 6
The average distance between two points in the grid is: 3.88889

[Program finished]
*/