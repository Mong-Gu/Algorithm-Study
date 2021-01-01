#include <iostream>
using namespace std;

string WHITE_BOARD[8] = {
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
};

string BLACK_BOARD[8] = {
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
	"BWBWBWBW",
	"WBWBWBWB",
};

string BOARD[51];

int calculate_cnt(int x, int y) {
	int white_cnt = 0;
	int black_cnt = 0;
	
	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			if (BOARD[i+x][j+y] != WHITE_BOARD[i][j])
				white_cnt++;
			if (BOARD[i+x][j+y] != BLACK_BOARD[i][j])
				black_cnt++;
		}
	}
	int min = (white_cnt >= black_cnt) ? black_cnt : white_cnt;
	return min;
}
 
int main()
{
	cin.tie(0);
	cout.tie(0);
	ios::sync_with_stdio(false);

	int n, m;
	int min = 999999;
	cin >> n >> m;

	for (int i = 0; i < n; i++)
		cin >> BOARD[i];

	for (int i = 0; i <= n - 8; i++) {
		for (int j = 0; j <= m - 8; j++) {
			int cnt = calculate_cnt(i, j);
			if (cnt < min)
				min = cnt;
		}
	}
	cout << min;
}


