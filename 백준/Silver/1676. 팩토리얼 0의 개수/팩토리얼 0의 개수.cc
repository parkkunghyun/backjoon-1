#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int n, cnt = 1 ; 

int main(){

   int n;
   int mul5 = 0;
   int mul25 = 0;
   int mul125 = 0;

    cin >> n;
    mul5 = n / 5;
    mul25 = n / 25;
    mul125 = n / 125;

    int k = mul125 + mul25 + mul5;
    cout << k << "\n";
    return 0;
}

