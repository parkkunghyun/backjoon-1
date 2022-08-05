#include<bits/stdc++.h>

using namespace std;

int t,n;

bool isPrime(int num) {
	
	for(int i = 2; i<num; i++) {
		if(num % i == 0) {
			return false;
		}
	}
	return true;

}
int answer(int num) {

	int len = num / 2;
	
	
	for(int i =0; i<len; i++) 
	{
		int temp = len - i;
		
		if(isPrime(temp)) {
			if(isPrime(num - temp)) {
				cout << temp << " " << num-temp << "\n";
				return 0;
			}
		}	
	}
	return 1;
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> t;
	
	for(int i =0; i<t; i++) {
		cin >> n;
		answer(n);
	}
	
	return 0;
}