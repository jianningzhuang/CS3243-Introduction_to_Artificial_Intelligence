/*
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
typedef vector<pair<int, int>> vii;

vector<vii> adj;
vector<int> dist;
unordered_map<int, int> pred;

int main(){
  int n, m;
  cin >> n >> m;
  adj.assign(n, vii());
  for (int i = 0; i < m; i++){
    int u, v, w;
    cin >> u >> v >> w;
    adj[u].push_back({v, w});
  }
  for (int i = 0; i < n; i++){
    if (i == 7){
      cout << -1 << endl;
      continue;
    }
    dist.assign(n, INF);
    dist[i] = 0;
    pred[i] = -1;
    set<pair<int, int>> pq;
    for (int j = 0; j < n; j++){
      pq.insert({dist[j], j});
    }
    while (!pq.empty()) {
      pair<int, int> p = *pq.begin();
      pq.erase(pq.begin());
      int d = p.first;
      int u = p.second;
      //cout << u << endl;
      if (u == 7){
        break;
      }
      for (auto &p1 : adj[u]) {
        int v = p1.first;
        int w = p1.second;
        if (dist[u]+w >= dist[v]) continue;
        pq.erase(pq.find({dist[v], v}));
        dist[v] = dist[u]+w;
        pred[v] = u;
        pq.insert({dist[v], v});
      }
    }
    int curr = 7;
    while (pred[curr] != i){
      curr = pred[curr];
    }
    cout << curr << endl;
  }
}
*/

#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int INF = 1e9; // INF = 1B, not 2^31-1 to avoid overflow

int main() {


  int V, E, s;
  cin >> V >> E >> s;
  vector<vii> AL(V, vii());
  while (E--) {
    int u, v, w;
    cin >> u >> v >> w;
    AL[u].emplace_back(v, w);                    // directed graph
  }

  vi dist(V, INF); dist[s] = 0;                  // INF = 1e9 here

  // Original Dijkstra's algorithm
  /*
  set<ii> pq;                                    // balanced BST version
  for (int u = 0; u < V; ++u)                    // dist[u] = INF
    pq.insert({dist[u], u});                     // but dist[s] = 0
  // sort the pairs by non-decreasing distance from s
  while (!pq.empty()) {                          // main loop
    auto [d, u] = *pq.begin();                   // shortest unvisited u
    pq.erase(pq.begin());
    for (auto &[v, w] : AL[u]) {                 // all edges from u
      if (dist[u]+w >= dist[v]) continue;        // not improving, skip
      pq.erase(pq.find({dist[v], v}));           // erase old pair
      dist[v] = dist[u]+w;                       // relax operation
      pq.insert({dist[v], v});                   // enqueue better pair
    }
  }
  */

  // (Modified) Dijkstra's algorithm
  priority_queue<ii, vector<ii>, greater<ii>> pq; pq.push({0, s});

  // sort the pairs by non-decreasing distance from s
  while (!pq.empty()) {                          // main loop
    auto [d, u] = pq.top(); pq.pop();            // shortest unvisited u
    if (d > dist[u]) continue;                   // a very important check
    for (auto &[v, w] : AL[u]) {                 // all edges from u
      if (dist[u]+w >= dist[v]) continue;        // not improving, skip
      dist[v] = dist[u]+w;                       // relax operation
      pq.push({dist[v], v});                     // enqueue better pair
    }
  }

  for (int u = 0; u < V; ++u)
    printf("SSSP(%d, %d) = %d\n", s, u, dist[u]);

  return 0;
}
