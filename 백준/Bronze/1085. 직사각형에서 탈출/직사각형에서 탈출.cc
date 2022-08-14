#include<iostream>
#include<algorithm>
#include<stack>
#include<string.h>
#include<math.h>
#include<vector>

using namespace std;

int x,y,w,h,mins;

int main() {
    cin >> x >> y >> w >> h;

    int min = 10001;

    if(x-0 < min) {
        min = x-0;
    }
    if(w-x < min) {
        min = w-x;
    }
    if(y - 0 < min) {
        min = y-0;
    }
    if(h-y < min) {
        min = h - y;
    }

    cout << min <<"\n";

    return 0;
}
