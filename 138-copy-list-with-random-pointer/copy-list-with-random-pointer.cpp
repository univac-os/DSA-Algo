/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
       //1st step add deep copy node in middle of original
        Node* itr,*front;
        itr=front=head;
        while(itr!=NULL){
            front=itr->next;
           Node* copy=new Node(itr->val);
            copy->next=front;
            itr->next=copy;
            itr=front;
       }
        
        //2nd step give same random val to deep copy
        itr=head;
        while(itr!=NULL){
            if(itr->random!=NULL){
                itr->next->random=itr->random->next;
            }
            itr=itr->next->next;  
        }
        
        // 3rd step is remove copy node from original
        itr=head;
        Node* pseudo=new Node(0);
        Node* pcopy=pseudo;
        while(itr!=NULL){
            front=itr->next->next;
            pcopy->next=itr->next;
            itr->next=front;
            
            pcopy=pcopy->next;
            itr=itr->next;
        }
        
        return pseudo->next;
        
    }
};