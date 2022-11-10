#include<bits/stdc++.h>

using namespace std;

int main() {
	int num;
	cin >> num;
	
	int cnt = num;
	int input[100] = {0,};
	for(int i =0; i<num; i++) {
		cin >> input[i];
		if(input[i] == 1)
			cnt--;
	}
	for(int i =0; i<num; i++) {
		for(int j = 2; j<= sqrt(input[i]); j++) {
			if(input[i] % j == 0) {
				cnt--;
				break;
			}
		}
	}
	cout << cnt;
	
	
	
	return 0;
}