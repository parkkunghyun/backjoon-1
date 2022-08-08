#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;


int main(){
	
	int t,n;
	string s;
	cin>>t;
	for(int i =0; i<t; i++) {
		cin >> n;
		cin >> s;
		string ap;
		
		for(int i =0; i<s.length(); i++) {
			for(int j =0; j<n; j++) {
				ap += s[i];
			}
		}
		
		cout << ap << endl;
	}
	return 0;
}