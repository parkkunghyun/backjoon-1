#include<bits/stdc++.h>

using namespace std;

int m,n,cnt, sum,mins;

bool isPrime(int n) {
		if(n <= 1) return false;
	
		for(int j =2; j<=sqrt(n); j++) {
			if(n% j == 0){
				return false;
			}
		}
		return true;
}

int main() {
	cin >> m >> n;
	
	sum = 0;
	mins = m;
	
	while(m <= n) {
		if(isPrime(m)) {
			mins = m;
			break;
		}
		m++;
	}
	
	while(m<=n) {
		
		if(isPrime(m) ) {
			sum += m;
		}
		m++;
	}
	
	if(sum == 0) cout << -1 << "\n";
	else {
		cout << sum << "\n";
		cout << mins << "\n";
	}
	
	return 0;
}

/*
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
	
	


*/