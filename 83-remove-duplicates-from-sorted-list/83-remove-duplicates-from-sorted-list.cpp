/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *p1, *p2;
        
        p1 = head;
        
        while(p1 != NULL && p1->next != NULL) {
            p2 = p1;
            
            while(p2->next != NULL) {
                if(p1->val == p2->next->val) {
                    p1->next = p2->next->next;
                } else {
                    p2 = p2->next;
                }
            }
            
            p1 = p1->next;
        }
        
        return head;
    }
};