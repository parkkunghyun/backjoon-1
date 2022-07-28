#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int cnt = 0;
void check(string a);

int main(){

    int n;
    cin >> n;
    string str;

    for(int i=0; i<n; i++) {
        cin>> str;
        check(str);
    }
    cout << cnt << '\n';
    return 0;
}
void check(string a) {
    int s = a.size();

    for(int i=0; i<s - 2; i++){

        if(a[i] != a[i+1] ){

            for(int j= i+2; j< s; j++){
                if(a[j] == a[i]) {
                    return;
                }
            }
        }
    }
    cnt++;
}
