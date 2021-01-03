#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;
 
int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    string str;
    cin >> str;
    transform(str.begin(), str.end(), str.begin(), ::toupper);
	int arr[26] = {0, };
    
    for (int i = 0; i < str.length(); i++)
    	arr[str[i] - 65] += 1;

	pair<int, int> first_max = make_pair(0, -1); // idx, value
	pair<int, int> second_max = make_pair(0, -2);
	
	for (int i = 0; i < 26; i++) {
		if (arr[i] > first_max.second) { 
			second_max = first_max;
			first_max.first = i;
			first_max.second = arr[i];
		}
		else if (arr[i] == first_max.second || arr[i] > second_max.second) {
			second_max.first = i;
			second_max.second = arr[i];
		}
	}
	
	if (first_max.second == second_max.second) cout << '?';
	else cout << (char)(first_max.first+65);

//	cout << (first_max.second == second_max.second) ? "?" : (char)(first_max.first+65); 이게 왜 안되지? 
}

