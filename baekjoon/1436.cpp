#include <iostream>
using namespace std;
 
int main()
{
    int n;
	cin >> n;
	int cnt = 0;
	int num = 1;
	string tmp;
	while (1) {
		tmp = to_string(num);
		if (tmp.find("666") != string::npos) {
			cnt++;
			if (cnt == n) {
				cout << tmp;
				return 0;
			}
		}
		num++;
	}
}

