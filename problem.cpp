#include <iostream>
#include <bits/stdc++.h>

const int N = 16;
const int INF = 1e9;
using namespace std;

int n, m;
vector<int> g[N];
vector < pair <int, int> > edges;

bool isIn(int bit, int mask) {
    return (bool) (1 << bit & mask);
}

int getEdgeCount(int mask) {
    int res = 0;
    for (int i = 0; i < edges.size(); i++) {
        int x = edges[i].first;
        int y = edges[i].second;
        res += (isIn(x, mask) && isIn(y, mask));
    }
    return res;
}

void dfs(int v, int mask, int &fx) {
    fx = fx | (1 << v);
    for (int i = 0; i < g[v].size(); i++) {
        int to = g[v][i];
        if (isIn(to, mask) && !isIn(to, fx)) {
            dfs(to, mask, fx);
        }
    }
}
int main()
{
    freopen("foo.txt", "r", stdin);
    cin >> n >> m;
    map <pair <int, int>, int > mp;
    for (int i = 1; i <= m; i++) {
        int x, y;
        cin >> y >> x;
        assert(x != y);
        x--; y--;
        if (x > y) swap(x, y);
        assert(mp.count({x, y}) == 0);
        mp[{x, y}] = 1;
        edges.push_back({x, y});
        g[x].push_back(y);
        g[y].push_back(x);
    }
    int ff = 0;
    dfs(0, (1 << n) - 1, ff);
    assert(ff == (1 << n) - 1);
    int ans = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int nodeCount = __builtin_popcount(mask);
        int firstNode = -1; 
        int edgeCount = getEdgeCount(mask);
        if (edgeCount != nodeCount - 1) continue;
        for (int i = 0; i < n; i++) {
            if (1 << i & mask) {
                firstNode = i;
            }
        }
        int fx = 0;
        dfs(firstNode, mask, fx);
        if (fx == mask) ans++;
    }
    cout << ans << endl;

}