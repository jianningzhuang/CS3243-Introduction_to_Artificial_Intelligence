#include <bits/stdc++.h>
using namespace std;

void print_vector(vector<string> s){
  for (auto i = s.begin(); i != s.end(); i++){
    cout << *i << " ";
  }
  cout << endl;
}

bool second(string a, string b){
  return a[1] < b[1];
}

bool last(string a, string b){
  return a.back() < b.back();
}


int main(){
  vector<string> s = {"Jianning", "Joshua", "Paul1", "Paul2", "Jackie"};
  print_vector(s);
  sort(s.begin(), s.end(), second); //stable?
  print_vector(s);
  sort(s.begin(), s.end(), last);
  print_vector(s);
}
