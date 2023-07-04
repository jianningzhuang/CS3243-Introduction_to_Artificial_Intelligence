#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  unordered_map<int, int> m;
  int result = 0;
  for (int i = 0; i < N; i++) {
    int h;
    cin >> h;
    if (m.find(h) == m.end()) {
      m[h] = 1;
      result++;
    }
    else {
      m[h]++;
      result++;
    }
    if (m.find(h+1) != m.end() && m[h+1] > 0) {
      m[h+1]--;
      result--;
    }
  }
  cout << result << endl;
}
