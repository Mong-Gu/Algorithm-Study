#include <iostream>

using namespace std;
 
int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

  	int a, b, v;
  	cin >> a >> b >> v;

	int day = (v - b - 1) / (a - b) + 1;
	cout << day;  	

    return 0;
}

