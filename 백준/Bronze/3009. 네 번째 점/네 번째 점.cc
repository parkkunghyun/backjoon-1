#include<iostream>
#include<algorithm>
#include<string>
#include<set>
#include<vector>
#include<stack>
#include<queue>

using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int x,y;
    int x1,y1,x2,y2,x3,y3;

    cin >> x1 >> y1 ;
    cin >> x2 >> y2 ;
    cin >> x3 >> y3 ;

    if(x1 == x2) {
        x = x3;
        
    }
    else if(x1 == x3) {
        x = x2;
    }else if (x2 == x3) {
        x = x1;
    }

     if(y1 == y2) {
        y = y3;
        
    }
    else if(y1 == y3) {
        y = y2;
    }else if (y2 == y3) {
        y = y1;
    }

    cout << x <<" " << y <<"\n";

    return 0;
}