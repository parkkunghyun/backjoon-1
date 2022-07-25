#include<bits/stdc++.h>

using namespace std;

int a[26],cnt, mindex=0;
string s;

int main(){

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> s;
	for(int i =0; i<s.size(); i++) {
	if(s[i]<97) a[s[i] - 65]++; //대문자 
	else a[s[i] - 97]++; //소문자

	}
	
	cnt = 0;
	int max = 0;
	
	for(int i =0; i<26; i++) {
		if(a[i] > max) {
			max = a[i];
			mindex = i;
		}
	}
	
	for(int i =0; i<26; i++) {
		if(max == a[i]) cnt++;
	}
	
	if(cnt > 1) cout<< "?" <<"\n";
	
	else cout<< (char)( mindex + 65 )<< "\n";
	
	return 0;
}