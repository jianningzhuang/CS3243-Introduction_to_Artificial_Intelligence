#include <bits/stdc++.h>
using namespace std;

struct Vertex{
  int item; //data stored in this vertex
  Vertex* next; //pointer to next vertex
};

class SLL{
private:
  Vertex* head;
  Vertex* tail;
public:
  SLL(){
    head = NULL; //initialize head to be NULL pointer
    tail = head;
  }
  Vertex* get(int i){
    Vertex* ptr = head; //start from head
    for (int j = 0; j < i; j++){ //advance i times
      ptr = ptr->next;
    }
    return ptr;
  }
  int search(int value){
    if (head == NULL){ //empty linked list
      return -1;
    }
    int index = 0;
    Vertex* temp = head; //start traversal
    while (temp->item != value){
      index++;
      temp = temp->next;
      if (temp == NULL){  //beyong tail
        return -1;
      }
    }
    return index;
  }
  void insert_empty(int value){
    Vertex* vtx = new Vertex(); //create new vertex
    vtx->item = value;
    vtx->next = head; //next vertex = NULL
    head = vtx; //head and tail both point to vtx
    tail = head;
  }
  void insert_head(int value){
    Vertex* vtx = new Vertex(); //create new vertex
    vtx->item = value; //set value
    vtx->next = head; // set pointer to next
    head = vtx; //vtx becomes new head,
  }
  void insert_tail(int value){
    Vertex* vtx = new Vertex();
    vtx->item = value;
    tail->next = vtx;
    tail = vtx;
  }
  void insert(int index, int value){
    if (head == NULL){
      insert_empty(value);
      return;
    }
    if (index == 0){  //if index = 0; call insert_head
      insert_head(value);
      return;
    }
    Vertex* pre = get(index - 1);  //traverse to the index - 1 vertex
    Vertex* aft = pre->next;  //aft cannot be null
    Vertex* vtx = new Vertex(); // create new vertex;
    vtx->item = value; //set value
    vtx->next = aft; //link
    pre->next = vtx; //link
  }
  void remove_head(){
    if (head == NULL){ //do nothing if LL is empty
      return;
    }
    Vertex* temp = head;  //keep track of old head to delete later
    head = head->next; //update new head
    delete temp;  //good practice to delete
  }
  void remove_tail(){
    if (head == NULL || head == tail){  //check LL has more than 1 item else switch to head removal
      remove_head();
      return;
    }
    Vertex* pre = head;
    Vertex* temp = head->next;
    while (temp->next != NULL){ //advance until temp is tail
      pre = pre->next;
      temp = temp->next;
    }
    pre->next = NULL;  //pre at the end of SLL
    delete temp; //delete old tail
    tail = pre; //update tail pointer
  }
  void remove(int index){
    Vertex* pre = get(index - 1);  //traverse to index - 1 vertex
    Vertex* del = pre->next; //del is vertex to delete
    Vertex* aft = del->next; //aft is vertex after del
    pre->next = aft; //bypass del
    delete del; //delete del
  }
  void print_ll(){
    Vertex* temp = head;
    while (temp != NULL){
      cout << temp->item << " ";
      temp = temp->next;
    }
    cout << endl;
  }
};

int main(){
  SLL l;
  l.insert(0,1);
  l.insert(0,2);
  l.insert_tail(4);
  l.insert(1,3);
  l.insert(3,5);
  l.insert_tail(6);
  l.print_ll();
  l.remove_head();
  l.remove_tail();
  l.remove(2);
  // l.remove_tail();
  // l.remove_tail();
  // l.remove_tail();
  // l.remove_tail();
  l.print_ll();
  cout << l.search(7);
}
