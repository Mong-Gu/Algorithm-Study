#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(string a, string b) {
	if (a.length() == b.length())
		return a < b;
	return a.length() < b.length();
}

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	int n;
	cin >> n;
	
	vector<string> v;
	string s;
	for (int i = 0; i < n; i++) {
		cin >> s;
		if (find(v.begin(), v.end(), s) == v.end())
			v.push_back(s);
	}
	sort(v.begin(), v.end(), compare);
	for(int i=0; i<v.size(); i++)
	    cout<<v[i]<<'\n';

}

