#include <iostream>
#include <algorithm>
using namespace std;
 
int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    int x, y, w, h;
    cin >> x >> y >> w >> h;
    
    int min_x = min(w - (w - x), w - x);
    int min_y = min(h - (h - y), h - y);
	int result = min(min_x, min_y);
	cout << result;

}

