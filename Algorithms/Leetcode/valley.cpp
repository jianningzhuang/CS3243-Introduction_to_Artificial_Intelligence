#include <bits/stdc++.h>
using namespace std;

int valley(vector<int> A, int l, int r) {
  if (r-l <= 1) {
    return min(A[l], A[r]);
  }
  int m = l + (r-l)/2;
  if (A[m] > A[m-1]) {
    return valley(A, l, m-1);
  }
  else if (A[m] > A[m+1]) {
    return valley(A, m+1, r);
  }
  else {
    return A[m];
  }
}

int main() {
  vector<int> A = {0,1};
  cout << valley(A, 0, 1) << endl;
}
