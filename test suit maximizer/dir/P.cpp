#include <iostream>
using namespace std;
int main()
{
    int a = 0, b = 0;
    cin >> a >> b;
    if (a >= 10000)
    {
        if (b >= 10000)
        {
            cout <<1<< "\n";
        }
        else if(b>=0)
        {
            cout <<2<< "\n";;
        }
        else 
        {
            cout <<3<< "\n";
        }
    }
    else if(a<=-10000)
    {
        if (b >= 0)
        {
            cout <<4<< "\n";
        }
        else
        {
            cout <<5<< "\n";
        }
    }
    else{
        
        if (b >= 100000)
        {
            cout <<6<< "\n";
        }
        else if(b <= -100000)
        {
            cout <<7<< "\n";
        }
        else{
            cout <<8<< "\n";
        }
    }
    return 0;
}