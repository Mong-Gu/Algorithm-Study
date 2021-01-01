#include <iostream>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	int arr[2][41] = {
			0,
	};
	arr[0][0] = 1;
	arr[1][1] = 1;
	for (int i = 2; i < 41; i++)
	{
		arr[0][i] = arr[0][i - 2] + arr[0][i - 1];
		arr[1][i] = arr[1][i - 2] + arr[1][i - 1];
	}

	int t, n;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> n;
		cout << arr[0][n] << ' ' << arr[1][n];
		if (i + 1 != t)
			cout << '\n';
	}

	return 0;
}
