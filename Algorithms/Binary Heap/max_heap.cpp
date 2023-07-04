#include <bits/stdc++.h>
using namespace std;

class Max_Heap{
private:
  vector<int> A;
public:
  Max_Heap(){
    A.push_back(0); // 0 index not used in a heap
  }
  bool is_leaf(int index){
    return index > heap_size()/2;
  }
  int left(int index){
    return index*2;
  }
  int right(int index){
    return index*2 + 1;
  }
  int parent(int index){
    return index/2;
  }
  int heap_size(){
    return A.size() - 1;
  }
  void max_heapify(int index){
    int l = left(index);
    int r = right(index);
    int largest = index;
    if (l <= heap_size() && A[l] > A[index]){
      largest = l;
    }
    if (r <= heap_size() && A[r] > A[largest]){
      largest = r;
    }
    if (largest != index){
      int temp;
      temp = A[index];
      A[index] = A[largest];
      A[largest] = temp;
      max_heapify(largest);
    }
  }
  void build_max_heap(vector<int> v){
    for (int i = 0; i < v.size(); i++){
      A.push_back(v[i]);
    }
    for (int i = heap_size()/2; i >= 1; i--){
      max_heapify(i);
    }
  }
  int max(){
    return A[1];
  }
  int extract_max(){
    int temp;
    temp = A[1];
    A[1] = A[heap_size()];
    A.pop_back();
    max_heapify(1);
    return temp;
  }
  void insert(int value){
    A.push_back(value);
    int index = heap_size();
    int parent = index/2;
    while (A[index] > A[parent]){
      int temp;
      temp = A[parent];
      A[parent] = A[index];
      A[index] = temp;
      index = parent;
      parent = index/2;
      if (index == 1){
        return;
      }
    }
  }
  void heap_sort(){
    while (heap_size() > 0){
      cout << extract_max() << " ";
    }
    cout << endl;
  }

  int rank(int value){
    return rank_recursive(value, 1);
  }
  int rank_recursive(int value, int index){
    int current_value = A[index];
    int sum = 0;
    if (current_value >= value){
      int l = left(index);
      int r = right(index);
      if (l <= heap_size()){
        sum += rank_recursive(value, l);
      }
      if (r <= heap_size()){
        sum += rank_recursive(value, r);
      }
      return sum + 1;
    }
    return sum;
  }
  void greater_than(int value){
    return g_recur(value, 1);
  }
  void g_recur(int value, int index){
    int current_value = A[index];
    if (current_value > value){
      cout << current_value << " ";
      int l = left(index);
      int r = right(index);
      if (l <= heap_size()){
        g_recur(value, l);
      }
      if (r <= heap_size()){
        g_recur(value, r);
      }
    }
    return;
  }
  int search(int value){  //returns index
    for (int i = 1; i < A.size(); i++){
      if (A[i] == value){
        return i;
      }
    }
    return -1;
  }
  void delete_key(int value){
    int index = search(value);
    int temp;
    temp = A[index];
    A[index] = A[heap_size()];
    A.pop_back();
    max_heapify(index);
    return;
  }
  void increase_key(int oldv, int newv){
    int index = search(oldv);
    A[index] = newv;
    if (index == 1){
      return;
    }
    int parent = index/2;
    while (A[index] > A[parent]){
      int temp;
      temp = A[parent];
      A[parent] = A[index];
      A[index] = temp;
      index = parent;
      parent = index/2;
      if (index == 1){
        return;
      }
    }

  }
  void print_heap(){
    for (int i = 1; i < A.size(); i++){
      cout << A[i] << " ";
    }
    cout << endl;
  }
};

int main(){
  vector<int> v = {2,8,14,16,7,4,1,3,9,10,11};
  Max_Heap h;
  h.build_max_heap(v);
  h.print_heap();
  cout << h.max() << endl;
  cout << h.extract_max() << endl;
  h.print_heap();
  h.insert(17);
  h.print_heap();
  cout << h.rank(7) << endl;
  h.greater_than(7);
  cout << endl;
  cout << h.search(10) << endl;
  cout << h.search(7) << endl;
  h.delete_key(7);
  h.print_heap();
  h.increase_key(10, 19);
  h.print_heap();
  h.heap_sort();
}
