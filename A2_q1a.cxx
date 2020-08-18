#include<iostream>
using namespace std;

int distance(int x1, int x2){
	if((x2-x1)>=0) return (x2-x1);
	else return (x1-x2);
}

int main(){
int n;
cout<<"To find the average distance between 2 points on a straight line made up of N discrete points having eqaul interval of 1 unit."<<endl<<endl;
cout<<"Enter the number(natural number) of points: ";
cin>>n;

float sum= 0, m=0;
if(n>0){
	for(int i=0; i<n; i++ ){
		for(int j=0; j<n; j++){
			sum=sum+distance(i,j);
			m++;
		}
	}
float avg;
avg = sum/m;

cout<<"The average distance between 2 points is "<<avg<<" unit."<<endl;
}
else cout<<"It is not possible to create a chain with the entered number of points. ";

return 0;
}

/*
output
To find the average distance between 2 points on a straight line made up of N discrete points having eqaul interval of 1 unit.

Enter the number(natural number) of points: 6
The average distance between 2 points is 1.94444 unit.

[Program finished]

*/