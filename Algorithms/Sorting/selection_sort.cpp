#include <bits/stdc++.h>
using namespace std;

void print_array(int arr[], int len){
  for (int i = 0; i < len; i++){
    cout << arr[i] << " ";
  }
  cout << endl;
}

// void selection_sort(int arr[], int len){
//   for (int i = 0; i < len - 1; i++){
//     int min = arr[i];
//     int to_swap = i;
//     for (int j = i + 1; j < len; j++){
//       if (arr[j] < min){
//         min = arr[j];
//         to_swap = j;
//       }
//     }
//     int temp;
//     temp = arr[i];
//     arr[i] = min;
//     arr[to_swap] = temp;
//   }
// }

void selection_sort(int arr[], int len){
  for (int i = 0; i < len - 1; i++){
    int x = min_element(arr + i, arr + len) - arr;
    swap(arr[x], arr[i]);
  }
}

int main(){
  int arr[] = {6,5,4,3,2,1};
  print_array(arr, 6);
  selection_sort(arr, 6);
  print_array(arr, 6);
}
