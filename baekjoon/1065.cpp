#include <iostream>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	int n;
	cin >> n;
	if (n < 100) {
		cout << n;
		return 0;
	}
	
	int arr[4];
	int cnt = 99;
	
	for (int i = 100; i <= n; i++) {
		int tmp = i;		
		int len = (tmp >= 100 && tmp < 1000) ? 3 : 4;
		int idx = len - 1;
		while (len) {
			arr[--len] = tmp % 10;
			tmp /= 10;
		}
		int gap = arr[1] - arr[0];
		bool check = true;
		for (int j = 0; j < idx; j++) {
			if (arr[j+1] - arr[j] != gap) {
				check = false;
				break;
			}
		}
		if (check)
			cnt++;
	}
	cout << cnt;
}
