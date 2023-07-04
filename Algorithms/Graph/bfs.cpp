#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

vector<vi> adj;
unordered_map<int, int> level;
unordered_map<int, int> parent;

void bfs(int s){
  level[s] = 0;
  parent[s] = -1;
  int l = 1;
  vector<int> frontier;
  frontier.push_back(s);
  while (!frontier.empty()){
    vector<int> next;
    for (auto &u : frontier){
      cout << u << endl;
      for (auto &v : adj[u]){
        if (level.find(v) == level.end()){
          level[v] = l;
          parent[v] = u;
          next.push_back(v);
        }
      }
    }
    frontier = next;
    l++;
  }
}

void path(int t){
  if (t == -1){
    return;
  }
  path(parent[t]);
  cout << t << " -> ";
}

void printlevels(){
  for (auto it = level.begin(); it != level.end(); it++){
    cout << it->first << " is at level " << it->second << endl;
  }
}

int main(){
  int n;
  cin >> n;
  adj.assign(n, vi());
  for (int i = 0; i < n; i++){  //number of vertices
    int k;
    cin >> k;
    for (int j = 0; j < k; j++){ //number of neighbours
      int end;
      cin >> end;
      adj[i].push_back(end);
      adj[end].push_back(i);
    }
  }
  bfs(0);
  path(7);
  printlevels();
}




#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> ii; // In this chapter, we will frequently use these
typedef vector<ii> vii; // three data type shortcuts. They may look cryptic
typedef vector<int> vi; // but shortcuts are useful in competitive programming

const int INF = 1e9; // INF = 1B, not 2^31-1 to avoid overflow

vi p;                                            // addition:parent vector

void printPath(int u) {                          // extract info from vi p
  if (p[u] == -1) { printf("%d", u); return; }
  printPath(p[u]);                               // output format: s -> ... -> t
  printf(" %d", u);
}

int main() {
  /*
  // Graph in Figure 4.3, format: list of unweighted edges
  // This example shows another form of reading graph input
  13 16
  0 1    1 2    2  3   0  4   1  5   2  6    3  7   5  6
  4 8    8 9    5 10   6 11   7 12   9 10   10 11  11 12
  */

  freopen("bfs_in.txt", "r", stdin);

  int V, E; scanf("%d %d", &V, &E);
  vector<vii> AL(V, vii());
  for (int i = 0; i < E; ++i) {
    int a, b; scanf("%d %d", &a, &b);
    AL[a].emplace_back(b, 0);
    AL[b].emplace_back(a, 0);
  }

  // as an example, we start from this source, see Figure 4.3
  int s = 5;

  // BFS routine inside int main() -- we do not use recursion
  vi dist(V, INF); dist[s] = 0;                  // INF = 1e9 here
  queue<int> q; q.push(s);
  p.assign(V, -1);                               // p is global

  int layer = -1;                                // for output printing
  bool isBipartite = true;                       // additional feature

  while (!q.empty()) {
    int u = q.front(); q.pop();
    if (dist[u] != layer) printf("\nLayer %d: ", dist[u]);
    layer = dist[u];
    printf("visit %d, ", u);
    for (auto &[v, w] : AL[u]) {                 // C++17 style, w ignored
      if (dist[v] == INF) {
        dist[v] = dist[u]+1;                     // dist[v] != INF now
        p[v] = u;                                // parent of v is u
        q.push(v);                               // for next iteration
      }
      else if ((dist[v]%2) == (dist[u]%2))       // same parity
        isBipartite = false;
    }
  }

  printf("\nShortest path: ");
  printPath(7), printf("\n");
  printf("isBipartite? %d\n", isBipartite);

  return 0;
}
