#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

long long a,b,c; 
long long temp,result;

long long go(long long a, long long b){
    if(b == 1) return a % c;
    long long _c = go(a, b/2);
    _c = (_c * _c) % c;
    if(b%2 == 1) _c = (_c * a) % c;
    return _c; 
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> a >> b >> c;

    cout << go(a,b)  << "\n";

    // 나눌때 반복되는 수들을 가지고 최대한 반복을 줄이는게 핵심인듯
    return 0;

}