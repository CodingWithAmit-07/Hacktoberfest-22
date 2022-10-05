#include<iostream>
using namespace std;

int main()
{
    
    int a = 6;
    int *b = &a;
    int **c = &b;
    cout<<c<<endl;
    cout<<&b;
    return 0;
}