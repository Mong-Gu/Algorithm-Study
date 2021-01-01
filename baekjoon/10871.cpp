#include <iostream>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	
	int N, X;
	cin >> N >> X;
	
	int arr[N];
	for (int i = 0; i < N; i++)
		cin >> arr[i];
	for (int j = 0; j < N; j++)
		if (arr[j] < X)
			cout << arr[j] << ' ';
}
