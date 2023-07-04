#include <bits/stdc++.h>
using namespace std;

vector<string> board;
vector<int> dr = {-1, 1, 0, 0};
vector<int> dc = {0, 0, 1, -1};
bool aflag = false;
int sizecc = 0;
int asize;
vector<int> land;

void dfs(int r, int c, int n, int m){
  sizecc++;
  if (board[r][c] == 'A'){
    aflag = true;
  }
  board[r][c] = '.';
  for (int i = 0; i < 4; i++){
    int rr = r + dr[i];
    int cc = c + dc[i];
    if (rr >= 0 && rr < n && cc >= 0 && cc < m){
      if (board[rr][cc] == '#' || board[rr][cc] == 'A'){
        dfs(rr, cc, n, m);
      }
    }
  }
}

int main(){
  int n, m, k;
  cin >> n >> m >> k;
  for (int i = 0; i < n; i++){
    string line;
    cin >> line;
    board.push_back(line);
  }
  for (int i = 0; i < n; i++){
    for (int j = 0; j < m; j++){
      if (board[i][j] == '#' || board[i][j] == 'A'){
        sizecc = 0;
        aflag = false;
        dfs(i, j, n, m);
        if (aflag){
          asize = sizecc;
        }
        else{
          land.push_back(sizecc);
        }
      }
    }
  }
  sort(land.begin(), land.end());
  int result = asize;
  for (int i = 0; i < k; i++){
    auto it = land.end();
    it--;
    result += *it;
    land.pop_back();
  }
  cout << result << endl;
}
