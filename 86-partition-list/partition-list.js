/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
var partition = function(head, x) {
    // Preserve the order, so use two linked lists and connect them
    const left = new ListNode();
    const right = new ListNode();
    let ltail = left;
    let rtail = right;
    
    while (head) {
        if (head.val < x) {
            // Add to the left list
            ltail.next = head;
            ltail = ltail.next;
        } else {
            // Add to the right list
            rtail.next = head;
            rtail = rtail.next;
        }
        head = head.next;
    }
    
    // Connect the end of the left list to the start of the right list
    ltail.next = right.next;
    // Set the end of the right list to null
    rtail.next = null;

    // Return the merged list
    return left.next;
};
