#include <iostream>
#include <deque>
#include <tuple>
#include <string.h>
using namespace std;

void BFS(deque<tuple<int, int, int>>& DQ, int field[][300], const int& I, const int& target_r, const int& target_c)
{
    pair<int, int> move[8] = {
        {2, -1}, {2, 1}, {1, -2}, {1, 2}, {-1, -2}, {-1, 2}, {-2, 1}, {-2, -1}
    };
    int now_r, now_c, step, to_r, to_c;

    while (!DQ.empty()) {
        tie(now_r, now_c, step) = DQ.front();
        DQ.pop_front();
        for (int to = 0; to < 8; to++) {
            to_r = now_r + move[to].first;
            to_c = now_c + move[to].second;
            if (0 <= to_r && to_r < I && 0 <= to_c && to_c < I && field[to_r][to_c] == 0) {
                field[to_r][to_c] = 1;
                if (to_r == target_r && to_c == target_c) {
                    cout << step + 1 << '\n';
                    DQ.clear();
                    return;
                }
                DQ.push_back(make_tuple(to_r, to_c, step + 1));
            }
        }
    }
}

int main()
{
    int T, I, start_r, start_c, target_r, target_c;
    cin >> T;
    int field[300][300];
    deque<tuple<int, int, int>> DQ;
    for (int tc = 0; tc < T; tc++) {
        memset(field, 0, sizeof(field));
        cin >> I >> start_r >> start_c >> target_r >> target_c;
        field[start_r][start_c] = 1;
        DQ.push_back(make_tuple(start_r, start_c, 0));
        if (start_r == target_r && start_c == target_c)
            cout << 0 << '\n';
        else
            BFS(DQ, field, I, target_r, target_c);
    }

    return 0;
}