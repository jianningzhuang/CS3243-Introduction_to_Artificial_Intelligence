#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9;

vector<vii> AL;
vector<vii> inverseAL;
vector<int> dist;
unordered_map<int, int> parent;
vector<int> status;
stack<int> topological;

int sp_dp(int v) {
  if (dist[v] != INF) {
    return dist[v];
  }
  for (auto &[u, w] : inverseAL[v]) {
    int new_distance = sp_dp(u) + w;
    if (new_distance < dist[v]) {
      dist[v] = new_distance;
      parent[v] = u;
    }
  }
  return dist[v];
}

void topological_sort(int u){
  status[u] = 1;
  for (auto &[v, w] : AL[u]){
    if (status[v] == 0){
      topological_sort(v);
    }
  }
  status[u] = 2;
  topological.push(u);
  cout << u << endl;
}

void sp_bottomup(int s) {
  topological_sort(s);
  while (!topological.empty()){
    int current = topological.top();
    for (auto &[v, w] : AL[current]) {
      int new_distance = dist[current] + w;
      if (new_distance < dist[v]) {
        dist[v] = new_distance;
        parent[v] = current;
      }
    }
    topological.pop();
  }
}

void path(int t){
  if (t == -1){
    return;
  }
  path(parent[t]);
  cout << t << " -> ";
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
  dist.assign(V, INF);
  dist[s] = 0; parent[s] = -1;

  for (int v = 0; v < V; v++) {
    sp_dp(v);
  }
  status.assign(V, 0);
  //sp_bottomup(s);

  for (int u = 0; u < V; ++u) {
    printf("SSSP(%d, %d) = %d\n", s, u, dist[u]);
  }

  return 0;
}
