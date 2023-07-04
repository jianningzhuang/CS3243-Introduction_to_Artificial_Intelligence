#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

struct hash_pair {
    template <class T1, class T2>
    size_t operator()(const pair<T1, T2>& p) const
    {
        auto hash1 = hash<T1>{}(p.first);
        auto hash2 = hash<T2>{}(p.second);
        return hash1 ^ hash2;
    }
};

vector<vii> AL;
vector<vii> inverseAL;
unordered_map<pair<int, int>, int, hash_pair> dist;
unordered_map<pair<int, int>, int, hash_pair> parent;

int sp_cycle_dp(int k, int v) {
  if (dist.find({k,v}) != dist.end()) {
    return dist[{k,v}];
  }
  dist[{k,v}] = INF;
  parent[{k,v}] = -1;
  for (auto &[u, w] : inverseAL[v]) {
    int new_distance = sp_cycle_dp(k-1, u) + w;
    if (new_distance < dist[{k,v}]) {
      dist[{k,v}] = new_distance;
      parent[{k,v}] = u;
    }
  }
  return dist[{k,v}];
}


int main() {

  int V, E, s;
  cin >> V >> E >> s;
  AL.assign(V, vii());
  inverseAL.assign(V, vii());
  while (E--) {
    int u, v, w;
    cin >> u >> v >> w;
    AL[u].emplace_back(v, w);
    inverseAL[v].emplace_back(u, w);
  }
  for (int i = 0; i < V; i++) {
    dist[{i,s}] = 0;
    parent[{i,s}] = -1;
  }
  for (int v = 0; v < V; v++) {
    if (v != s) {
      dist[{0, v}] = INF;
    }
  }
  for (int v = 0; v < V; v++) {
    sp_cycle_dp(V-1, v);
  }

  for (int u = 0; u < V; ++u) {
    printf("SSSP(%d, %d) = %d\n", s, u, dist[{V-1,u}]);
  }

  return 0;
}
