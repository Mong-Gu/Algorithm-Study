#include <iostream>

using namespace std;

int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);
	
	int year;
	cin >> year;
	
	if (year % 4 == 0 && ((year % 100 != 0) || (year % 400 == 0))) { // À±³âÀÏ ¶§ 
		cout << 1;
	} else {
		cout << 0;
	}
}
