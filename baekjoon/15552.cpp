#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int T, A, B;
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		cin >> A >> B;
		cout << A + B << '\n';
	}
	return 0;
}
