#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;

vector<vi> adj;
vi status;   //0 is unvisited, 1 is explored, 2 is visited
unordered_map<int, int> parent;
unordered_map<int, string> edges;
stack<int> topological;

void dfs(int u){
  cout << u << endl;
  status[u] = 1;
  for (auto &v : adj[u]){
    if (status[v] == 0){
      parent[v] = u;
      edges[u*10 + v] = "tree";
      dfs(v);
    }
    else if (status[v] == 1){
      edges[u*10 + v] = "back";
      cout << "cyclic\n";
    }
    else{
      edges[u*10 + v] = "cross";
    }
  }
  status[u] = 2;
  topological.push(u);
}

void printedges(){
  for (auto it = edges.begin(); it != edges.end(); it++){
    cout << it->first << " is  a " << it->second << " edge\n";
  }
}

void path(int t){
  if (t == -1){
    return;
  }
  path(parent[t]);
  cout << t << " -> ";
}

int main(){
  int n;
  cin >> n;
  adj.assign(n, vi());
  status.assign(n, 0);
  for (int i = 0; i < n; i++){  //number of vertices
    int k;
    cin >> k;
    for (int j = 0; j < k; j++){ //number of neighbours
      int end;
      cin >> end;
      adj[i].push_back(end);
    }
  }
  parent[0] = -1;
  dfs(0);
  path(3);
  printedges();
  cout << endl;
  cout << topological.size() << endl;
  while (!topological.empty()){
    cout << topological.top() << " ";
    topological.pop();
  }
}
