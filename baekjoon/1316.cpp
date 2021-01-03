#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;
 
int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

	int n;
	cin >> n;
	int cnt = 0;

	for (int i = 0; i < n; i++) {
		int visited[26] = { 0, };
		bool check = 1;
		string word;
		cin >> word;
		
		visited[word[0]-97] = 1;
		for (int j = 1; j < word.length(); j++) {
			if (word[j] != word[j-1] && visited[word[j]-97]) {
				check = 0;
				break;
			}
			visited[word[j]-97]++;
		}
		if (check) cnt++;
	}	
	cout << cnt;
}

