#include <bits/stdc++.h>
using namespace std;

struct BSTVertex{
  BSTVertex* parent;
  BSTVertex* left;
  BSTVertex* right;
  int key;
  int height;
};

class BST{
protected:
  BSTVertex* root;

  BSTVertex* insert(BSTVertex* T, int v){
    if (T == NULL){  //includes inserting into empty BST
      T = new BSTVertex;
      T->key = v;
      T->parent = NULL;
      T->left = NULL;
      T->right = NULL;
      T->height = 0;
    }
    else if (T->key < v){
      T->right = insert(T->right, v);
      T->right->parent = T;
    }
    else{
      T->left = insert(T->left, v);
      T->left->parent = T;
    }
    return T;
  }

  void inorder(BSTVertex* T){
    if (T == NULL){
      return;
    }
    inorder(T->left);
    cout << T->key << " ";
    inorder(T->right);
  }

  void preorder(BSTVertex* T){
    if (T == NULL){
      return;
    }
    cout << T->key << " ";
    preorder(T->left);
    preorder(T->right);
  }

  int findMin(BSTVertex* T){
    if (T == NULL){
      return -1;
    }
    else if (T->left == NULL){
      return T->key;
    }
    else{
      return findMin(T->left);
    }
  }

  int findMax(BSTVertex* T){
    if (T == NULL){
      return -1;
    }
    else if (T->right == NULL){
      return T->key;
    }
    else{
      return findMax(T->right);
    }
  }

  BSTVertex* search(BSTVertex* T, int v){
    if (T == NULL){
      return T;
    }
    else if (T->key == v){
      return T;
    }
    else if (T->key < v){
      return search(T->right, v);
    }
    else{
      return search(T->left, v);
    }
  }

  int successor(BSTVertex* T){
    if (T->right != NULL){
      return findMin(T->right);
    }
    else{
      BSTVertex* par = T->parent;
      BSTVertex* cur = T;
      while ((par != NULL) && (cur == par->right)){
        cur = par;
        par = cur->parent;
      }
      if (par == NULL){
        return -1;
      }
      else{
        return par->key;
      }
    }
  }

  int predecessor(BSTVertex* T){
    if (T->left != NULL){
      return findMax(T->left);
    }
    else{
      BSTVertex* par = T->parent;
      BSTVertex* cur = T;
      while ((par != NULL) && (cur == par->left)){
        cur = par;
        par = cur->parent;
      }
      if (par == NULL){
        return -1;
      }
      else{
        return par->key;
      }
    }
  }

  BSTVertex* remove(BSTVertex* T, int v){
    if (T == NULL){
      return T;
    }
    if (T->key == v){
      if (T->left == NULL && T->right == NULL){
        T = NULL;
      }
      else if (T->left == NULL && T->right != NULL){
        T->right->parent = T->parent;
        T = T->right;
      }
      else if (T->left != NULL && T->right == NULL){
        T->left->parent = T->parent;
        T = T->left;
      }
      else{
        int successorV = successor(v);
        T->key = successorV;
        T->right = remove(T->right, successorV);
      }
    }
    else if (T->key < v){
      T->right = remove(T->right, v);
    }
    else{
      T->left = remove(T->left, v);
    }
    return T;
  }

  int getHeight(BSTVertex* T){
    if (T == NULL){
      return -1;
    }
    else{
      return max(getHeight(T->left), getHeight(T->right)) + 1;
    }
  }
public:
  BST(){
    root = NULL;
  }

  void insert(int v){
    root = insert(root, v);
  }
  void inorder(){
    inorder(root);
    printf("\n");
  }

  void preorder() {
    preorder(root);
    printf("\n");
  }

  int findMin() { return findMin(root); }

  int findMax() { return findMax(root); }

  int search(int v) {
    BSTVertex* res = search(root, v);
    return res == NULL ? -1 : res->key;
  }

  int successor(int v) {
    BSTVertex* vPos = search(root, v);
    return vPos == NULL ? -1 : successor(vPos);
  }

  int predecessor(int v) {
    BSTVertex* vPos = search(root, v);
    return vPos == NULL ? -1 : predecessor(vPos);
  }

  void remove(int v) { root = remove(root, v); }

  // will be used in AVL lecture
  int getHeight() { return getHeight(root); }
  };

  // int main() {
  //   BST* T = new BST();                                            // an empty BST
  //
  //   printf("%d\n", T->findMin());                                 // not found, -1
  //   printf("%d\n", T->findMax());                                 // not found, -1
  //
  //   // Sample BST as shown in Lecture
  //   T->insert(15);
  //   T->insert(23);
  //   T->insert(6);
  //   T->insert(71);
  //   T->insert(50);
  //   T->insert(4);
  //   T->insert(7);
  //   T->insert(5);
  //
  //   printf("%d\n", T->findMin());                                             // 4
  //   printf("%d\n", T->findMax());                                            // 71
  //
  //   cout << T->search(71) << endl;                                   // found, 71
  //   printf("%d\n", T->search(7));                                      // found, 7
  //   printf("%d\n", T->search(22));                                // not found, -1
  //
  //   T->inorder();                           // The BST: 4, 5, 6, 7, 15, 23, 50, 71
  //   T->preorder();
  //   printf("%d\n", T->getHeight());                                           // 3
  //
  //   printf("%d\n", T->successor(23));                                        // 50
  //   printf("%d\n", T->successor(7));                                         // 15
  //   printf("%d\n", T->successor(71));                                        // -1
  //   printf("%d\n", T->predecessor(23));                                      // 15
  //   printf("%d\n", T->predecessor(7));                                        // 6
  //   printf("%d\n", T->predecessor(71));                                      // 50
  //
  //   printf("Removing 5\n");
  //   T->remove(5);
  //   printf("Removing 71\n");
  //   T->remove(71);
  //   printf("Removing 15\n");
  //   T->remove(15);
  //
  //   T->inorder();                                      // The BST: 4, 6, 7, 23, 50
  //   printf("%d\n", T->getHeight());                                           // 2
  //
  //   return 0;
  // }
