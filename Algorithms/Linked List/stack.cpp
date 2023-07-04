#include <bits/stdc++.h>
using namespace std;

struct Vertex{
  int item; //data stored in this vertex
  Vertex* next; //pointer to next vertex
};

class Stack{
private:
  Vertex* head;
  Vertex* tail;
public:
  Stack(){
    head = NULL; //initialize head to be NULL pointer
    tail = head;
  }
  void peek(){
    if (head != NULL){
      cout << head->item << endl;;
    }
    else{
      cout << "empty stack\n";
    }
  }

  void insert_empty(int value){
    Vertex* vtx = new Vertex(); //create new vertex
    vtx->item = value;
    vtx->next = head; //next vertex = NULL
    head = vtx; //head and tail both point to vtx
    tail = head;
  }
  void insert_head(int value){
    if (head == NULL){
      insert_empty(value);
      return;
    }
    Vertex* vtx = new Vertex(); //create new vertex
    vtx->item = value; //set value
    vtx->next = head; // set pointer to next
    head = vtx; //vtx becomes new head,
  }
  void remove_head(){
    if (head == NULL){ //do nothing if LL is empty
      return;
    }
    Vertex* temp = head;  //keep track of old head to delete later
    head = head->next; //update new head
    delete temp;  //good practice to delete
  }
  void print_stack(){
    Vertex* temp = head;
    while (temp != NULL){
      cout << temp->item << " ";
      temp = temp->next;
    }
    cout << endl;
  }
};



int main(){
  Stack s;
  s.peek();
  s.insert_head(2);
  s.insert_head(4);
  s.insert_head(1);
  s.insert_head(2);
  s.print_stack();
  s.remove_head();
  s.remove_head();
  s.print_stack();

  stack<int> stl;
  stl.push(2);
  stl.push(4);
  stl.push(1);
  stl.push(3);
  cout << stl.top() << endl;

}
