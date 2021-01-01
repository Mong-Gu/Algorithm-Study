#include <iostream>
#include <vector>

using namespace std;
 
int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    int n;
    cin >> n;
    string data;
    for (int i = 0; i < n; i++) {
    	cin >> data;
    	vector <char> v;

    	for (int j = 0; j < data.length(); j++) {
    		if (v.empty()) {
    			v.push_back(data[j]);
    			continue;
			}
			if (data[j] == ')' && data[j] != v.back()) {
				v.pop_back();
				continue;
			}
			v.push_back(data[j]);
		}
		cout << (v.empty() ? "YES\n" : "NO\n");
	}

    return 0;
}

