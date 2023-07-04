#include <bits/stdc++.h>
using namespace std;

void print_vector(vector<long long> &v){
  for (auto i = v.begin(); i != v.end(); i++){
    cout << *i << " ";
  }
  cout << endl;
}

long long max(vector<long long> &v){
  long long max_val = v[0];
  for (auto i = v.begin(); i != v.end(); i++){
    if (*i > max_val){
      max_val = *i;
    }
  }
  return max_val;
}

void counting_sort(vector<long long> &v, int size, int exp){
  vector<long long> frequency;
  for (int i = 0; i < 10; i++){
    frequency.push_back(0);
  }
  vector<long long> final;
  for (int i = 0; i < size; i++){
    final.push_back(0);
  }
  for (int i = 0; i < size; i++){
    frequency[(v[i]/exp)%10]++;
  }
  for (int i = 1; i < 10; i++){
    frequency[i] += frequency[i - 1];
  }
  for (int i = size - 1; i >= 0; i--){
    final[frequency[(v[i]/exp)%10] - 1] = v[i];
    frequency[(v[i]/exp)%10]--;
  }
  for (int i = 0; i < size; i++){
    v[i] = final[i];
  }

}

void radix_sort(vector<long long> &v){
  long long maximum = max(v);
  for (int exp = 1; maximum/exp > 0; exp *= 10){
    counting_sort(v, v.size(), exp);
  }
}

int main(){
  vector<long long> v;
  v.push_back(170);
  v.push_back(5);
  v.push_back(11111111111111);
  v.push_back(2);
  radix_sort(v);
  print_vector(v);
}
