#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int N, M;
    cin >> M >> N;
    const vector<pair<int, int>> directions{ {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
    queue<pair<int, int>> Q;
    int field[1000][1000];
    int zero = 0;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            cin >> field[r][c];
            if (field[r][c] == 1)
                Q.push(make_pair(r, c));
            else if (field[r][c] == 0)
                zero++;
        }
    }

    int row, col, y, x, cnt = 0;
    while (Q.size()) {
        row = Q.front().first;
        col = Q.front().second;
        Q.pop();
        for (const pair<int, int>& dir : directions) {
            y = row + dir.first;
            x = col + dir.second;
            if (0 <= y && y < N && 0 <= x && x < M and field[y][x] == 0) {
                field[y][x] = field[row][col] + 1;
                cnt++;
                Q.push(make_pair(y, x));
            }
        }
    }

    if (cnt != zero) {
        cout << -1;
        return 0;
    }

    int max_val = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            if (max_val < field[i][j])
                max_val = field[i][j];

    cout << max_val - 1;
    return 0;
}