/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* current2 = headB;
        
        while(headA != NULL) {
            current2 = headB;
            while(current2 != NULL) {
                if(headA == current2) return headA;
                current2 = current2->next;
            }
            headA = headA->next;
        }
        
        return NULL;
    }
};