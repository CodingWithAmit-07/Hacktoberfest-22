#include<iostream>
using namespace std;

typedef struct worker
{
    int id;
    char dem;
    float salary;
}dm;

int main()
{
    dm ram;
    ram.id=7;
    ram.dem='a';
    ram.salary=7777777;
    
    cout<<ram.id<<endl;
    cout<<ram.dem<<endl;
    cout<<ram.salary<<endl;
    return 0;
}