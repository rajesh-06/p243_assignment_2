#include<iostream>
using namespace std;

int main(){
float A[3]={7.2, 3, 5};
float B[3]={3,-4,6};
cout<<"A=(7.2, 3, 5)"<<endl;
cout<<"B=(3,-4,6)"<<endl;

//Summation of 2 vector(A+B)
cout<<"A+B = (";
for(int j=0; j<2; j++){
	cout<<A[j]+B[j]<<", ";
}cout<<A[2]+B[2]<<")" <<endl;

//Dot product
float sum=0.0;
for(int i=0; i<3; i++){
	sum=sum+A[i]*B[i];
}
cout<<"Dot product of A and B(A.B) is "<<sum<<"."<<endl;

return 0;
}

/*
Output
A=(7.2, 3, 5)
B=(3,-4,6)
A+B = (10.2, -1, 11)
Dot product of A and B(A.B) is 39.6.

[Program finished]
*/