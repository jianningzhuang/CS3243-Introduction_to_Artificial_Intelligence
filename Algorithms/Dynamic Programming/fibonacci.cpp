#include <bits/stdc++.h>
using namespace std;


int fib(int n) {
  if (n <= 2) {
    return 1;
  }
  else {
    return fib(n-1) + fib(n-2);
  }
}

unordered_map<int, int> memo;

int fib_memo(int n) {
  if (memo.find(n) != memo.end()) {
    cout << "found" << endl;
    return memo[n];
  }
  else if (n <= 2) {
    return 1;
  }
  else {
    int f = fib_memo(n-1) + fib_memo(n-2);
    memo[n] = f;
    return f;
  }
}

int fib_bottomup(int n) {
    // Declare an array to store
    // Fibonacci numbers.
    // 1 extra to handle
    // case, n = 0
    vector<int> f;
    f.assign(n+1, 0);

    // 0th and 1st number of the
    // series are 0 and 1
    f[0] = 0;
    f[1] = 1;

    for(int i = 2; i <= n; i++) {

       //Add the previous 2 numbers
       // in the series and store it
       f[i] = f[i - 1] + f[i - 2];
    }
    return f[n];
}


int main() {
  for (int i = 1; i < 10; i++) {
    cout << fib(i) << endl;
  }
  for (int i = 1; i < 10; i++) {
    cout << fib_memo(i) << endl;
  }
  for (int i = 1; i < 10; i++) {
    cout << fib_bottomup(i) << endl;
  }
}
