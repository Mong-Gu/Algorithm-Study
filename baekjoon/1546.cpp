#include <iostream>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	int n;
	int m = -1;
	cin >> n;
	float score[n];
	for (int i = 0; i < n; i++) {
		cin >> score[i];
		if (score[i] > m)
			m = score[i];
	}
	float total = 0;
	for (int i = 0; i < n; i++) {
		score[i] = score[i]/m*100;
		total += score[i];
	}
	cout << fixed;
	cout.precision(2);
	cout << total / n;
}
