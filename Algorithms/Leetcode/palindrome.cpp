#include <bits/stdc++.h>
using namespace std;


//put in vector and compare
int main() {
  int x = 121;
  vector<int> v1;
  if (x == 0) {
    return true;
  }
  if (x < 0) {
    return false;
  }
  while (x > 0) {
    v1.push_back(x%10);
    x/=10;
  }
  for (int i = 0; i < v1.size()/2; i++) {
    if (v1[i] != v1[v1.size()-1-i]) {
      return false;
    }
  }
  return true;

}

bool isPalindrome(int x) {
  vector<int> v1;
  if (x == 0) {
    return true;
  }
  if (x < 0 || x%10 == 0) {
    return false;
  }
  int revertednum = 0;
  while (x > revertednum) {
    revertednum = revertednum*10 + x%10;
    x/=10;
  }
  return x == revertednum || x == revertednum/10;
}
