#include <bits/stdc++.h>
using namespace std;

void print_vector(vector<long long> &v){
  for (auto i = v.begin(); i != v.end(); i++){
    cout << *i << " ";
  }
  cout << endl;
}

void counting_sort(vector<long long> &v, int size, int exp){
  map<int, vector<long long>> buckets;
  for (int i = 0; i < size; i++){
    vector<long long> bucket;
    buckets[i] = bucket;
  }
  for (int i = 0; i < size; i++){
    buckets[(v[i]/exp)%size].push_back(v[i]);
  }
  v.clear();
  for (int i = 0; i < size; i++){
    for (auto j = buckets[i].begin(); j != buckets[i].end(); j++){
      v.push_back(*j);
    }
  }
}

void radix_sort(vector<long long> &v){
  auto max = max_element(v.begin(), v.end());
  for (long long exp = 1; *max/exp > 0; exp *= v.size()){
    counting_sort(v, v.size(), exp);
  }
}

int main(){
  vector<long long> v = {11111111, 222, 333333333333, 44, 5, 5};
  print_vector(v);
  radix_sort(v);
  print_vector(v);
}
