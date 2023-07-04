#include <iostream>
using namespace std;

void print_array(int arr[], int len){
  for (int i = 0; i < len; i++){
    cout << arr[i] << " ";
  }
  cout << endl;
}

int partition(int arr[], int start, int end){
  int pivot = arr[start];
  int m = start; //left and right initially empty
  for (int k = start + 1; k <= end; k++){
    if (arr[k] < pivot){
      m++; //increment m to slot in new element in left
      int temp;
      temp = arr[m];
      arr[m] = arr[k];
      arr[k] = temp;  //swap first elem in right with new element in left to maintain sorted invariant
    }
  }
  int temp;
  temp = arr[start];
  arr[start] = arr[m];
  arr[m] = temp;
  return m;
}

void quicksort(int arr[], int low, int high){
  if (low < high){
    int m = partition(arr, low, high);//O(N)
    quicksort(arr, low, m - 1);
    quicksort(arr, m + 1, high);
  }

}

int main(){
  int arr[] = {6,5,4,3,2,1};
  print_array(arr, 6);
  quicksort(arr, 0, 5);
  print_array(arr, 6);
}
