#include <bits/stdc++.h>
using namespace std;

struct Vertex{
  int item; //data stored in this vertex
  Vertex* next; //pointer to next vertex
};

class Queue{
private:
  Vertex* head;
  Vertex* tail;
public:
  Queue(){
    head = NULL; //initialize head to be NULL pointer
    tail = head;
  }
  void insert_empty(int value){
    Vertex* vtx = new Vertex(); //create new vertex
    vtx->item = value;
    vtx->next = head; //next vertex = NULL
    head = vtx; //head and tail both point to vtx
    tail = head;
  }
  void insert_tail(int value){
    if (head == NULL){
      insert_empty(value);
      return;
    }
    Vertex* vtx = new Vertex();
    vtx->item = value;
    tail->next = vtx;
    tail = vtx;
  }
  void remove_head(){
    if (head == NULL){ //do nothing if LL is empty
      return;
    }
    Vertex* temp = head;  //keep track of old head to delete later
    head = head->next; //update new head
    delete temp;  //good practice to delete
  }
  void print_queue(){
    Vertex* temp = head;
    while (temp != NULL){
      cout << temp->item << " ";
      temp = temp->next;
    }
    cout << endl;
  }
};

int main(){
  Queue s;
  s.insert_tail(2);
  s.insert_tail(4);
  s.insert_tail(1);
  s.insert_tail(2);
  s.print_queue();
  s.remove_head();
  s.remove_head();
  s.print_queue();



}
