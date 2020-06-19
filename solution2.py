/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()

{
    long a=0,b=1,count=0;
    long c=0;
    for(long i=1;c<=4000000;i++)
    {
        c=a+b;
        if (c%2==0)
        {
            count= count+ c;
        }
        a=b;
        b=c;
    }
    cout<<count;
    return 0;
}
