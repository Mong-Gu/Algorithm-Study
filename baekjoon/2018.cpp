#include <iostream>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int end = 1;
	int total = 0;
	int cnt = 0;
	
	for (int start = 1; start <= n; start++) {
		while (total < n && end <= n) {
			total += end;
			end++;
		}
		if (total == n)
			cnt++;
		total -= start;
	}
	
	cout << cnt;
}
