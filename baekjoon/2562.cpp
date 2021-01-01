#include <iostream>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	int m = -1;
	int idx = 0;
	int tmp;
	for (int i = 0; i < 9; i++) {
		cin >> tmp;
		if (tmp > m) {
			m = tmp;
			idx = i;
		}
	}	
	cout << m << '\n' << idx + 1;
}
