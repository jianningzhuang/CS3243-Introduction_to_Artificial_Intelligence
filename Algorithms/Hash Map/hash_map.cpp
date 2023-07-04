#include <bits/stdc++.h>
using namespace std;

const int M = 13;

class hash_table{
private:
  list<pair<string, int>> table[M]; //array of M linked lists

  int hash_function(string v){  //string only contains uppercase
    int index = 0;
    for (auto &c : v){
      index = ((index*26)%M + (c - 'A' + 1))%M;
    }
    return index;
  }
public:
  hash_table(){
    for (int i = 0; i < M; i++){
      table[i].clear();  //clear each linked list
    }
  }

  void insert(string key, int value){
    bool found = false;
    for (auto &p : table[hash_function(key)]){  //for each (key, value) pair in linked list
      if (p.first == key){
        found = true;
        p.second = value;  //updates value
      }
    }
    if (!found){
      table[hash_function(key)].emplace_back(key, value);
    }
  }

  int search(string key){
    for (auto &p : table[hash_function(key)]){
      if (p.first == key){
        return p.second; //returns satellite data
      }
    }
    return -1;
  }

  void remove(string key){
    auto &row = table[hash_function(key)];
    for (auto it = row.begin(); it != row.end(); it++){
      if (it->first == key){
        row.erase(it);
        break;
      }
    }
  }

  bool is_empty(){
    int total = 0;
    for (int i = 0; i < M; i++){
      total += int(table[i].size());
    }
    return (total == 0);
  }
};

int main(){
  hash_table ht;
  cout << ht.is_empty() << endl;

  ht.insert("STEVEN", 77);
  cout << ht.is_empty() << endl;

  cout << ht.search("STEVEN") << endl;
  ht.insert("STEVEN", 38);
  cout << ht.search("STEVEN") << endl;

  ht.remove("STEVEN");
  cout << ht.search("STEVEN") << endl;

  unordered_map<string, int> mapper;
  cout << mapper.empty() << endl;

  mapper["STEVEN"] = 38;
  cout << mapper["STEVEN"] << endl;
  cout << (mapper.find("STEVEN") == mapper.end() ? -1 : 1) << endl;
  mapper.erase("STEVEN");
  cout << (mapper.find("STEVEN") == mapper.end() ? -1 : 1) << endl;

}
