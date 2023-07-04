#include <bits/stdc++.h>
using namespace std;

vector<int> nums = {2, 7, 11, 15};
int target = 9;

void print_vector(vector<pair<int, int>> v){
  for (auto i = v.begin(); i != v.end(); i++){
    cout << i->first << i->second << endl;
  }
}

//hashmap O(n)
int main() {
  vector<int> result = {0, 0};
  unordered_map<int, int> m;
  for (int i = 0; i < nums.size(); i++) {
    if (m.find(target-nums[i]) == m.end()) {
      m.insert({nums[i],i});
    }
    else {
      cout << m[target-nums[i]] << i << endl;
      return 0;
    }
  }
}


//O(nlogn) sort + O(n) 2 pointer
/*
int main() {
  vector<int> result = {0, 0};
  vector<pair<int, int>> v;
  for (int i = 0; i < nums.size(); i++) {
    v.push_back({nums[i], i});
  }
  sort(v.begin(), v.end());
  vector<pair<int, int>>::iterator low = v.begin();
  vector<pair<int, int>>::iterator high = v.end()-1;
  while (1) {
    if (low->first + high->first == target) {
      cout << low->second << high->second << endl;
      return 0;
    }
    else if (low->first + high->first < target) {
      low++;
    }
    else if (low->first + high->first > target) {
      high--;
    }

  }
  print_vector(v);
}
*/
