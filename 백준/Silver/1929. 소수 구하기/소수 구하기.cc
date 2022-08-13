#include<iostream>
#include<algorithm>
#include<stack>
#include<string.h>
#include<math.h>
#include<vector>

using namespace std;

#define MAX 1000000
int arr[MAX + 1]={0,};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int m,n;
    cin >> m >> n;

    vector<int> arr(n+1, 0);
    for(int i =2; i<= n; i++) {
        arr[i] = i;
    }
    for(int i = 2; i*i <= n; i++) {
        if(arr[i] == 0)continue;
        for(int j =2 * i; j<= n; j+= i) {
            if(arr[j] == 0) continue;
            else arr[j] = 0;
        }
    }
    for(int i =m; i<=n; i++) {
        if(arr[i] != 0) printf("%d\n", arr[i]);
    }

    return 0;
}