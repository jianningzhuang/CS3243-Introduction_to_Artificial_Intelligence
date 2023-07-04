#include <iostream>
using namespace std;

void print_array(int arr[], int len){
  for (int i = 0; i < len; i++){
    cout << arr[i] << " ";
  }
  cout << endl;
}


void insertion_sort(int arr[], int len){
  for (int i = 1; i < len; i++){
    int x = arr[i];
    int j = i - 1;
    for (j; j >= 0 && arr[j] > x; j--){
      arr[j+1] = arr[j];
    }
    arr[j+1] = x;
  }
}

int main(){
  int arr[] = {6,5,4,3,2,1};
  print_array(arr, 6);
  insertion_sort(arr, 6);
  print_array(arr, 6);

}
