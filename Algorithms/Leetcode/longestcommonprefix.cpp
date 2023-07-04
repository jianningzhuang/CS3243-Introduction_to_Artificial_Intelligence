#include <bits/stdc++.h>
using namespace std;

vector<string> strs = {"flower","flow","flight"};

int main() {
  string common = "";
  for (int i = 0; i < strs[0].size(); i++) {
    string current = common + strs[0][i];
    for (int j = 0; j < strs.size(); j++) {
      if (strs[j].find(current) != 0) {
        cout << common << endl;
        return common;
      }
    }
    common = current;
  }
  return common;
}
