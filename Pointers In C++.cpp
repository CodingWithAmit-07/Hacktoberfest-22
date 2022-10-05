#include<iostream>
using namespace std;
int main()
{
	int a = 7;
	int *b = &a; 
	int **c = &b;
	cout<<b<<endl;       //Pointer tell the address of the particular data type
	
	cout<<&a<<endl;
	
	cout<<*b<<endl;       //Here * tell the value of the data type 
	cout<<c;	
	
	return 0;
}
