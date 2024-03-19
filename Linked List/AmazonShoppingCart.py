# AWS Software Development Engineer Full-Time Opportunity (Online Assessment)
# Tags: linkedlistlc, amazon, interviewlc

# Items in a shopping cart are represented as instances of SinglyLinkedListNode
    # each node instances has the following properties:
        # data (string): the item name
        # next: the pointer to the next node
# Initially, your cart has n items
# You can perform the following operations on your cart:
    # PUSH_HEAD itemName: insert a new item with data = itemName as the head of the linked list
    # PUSH_TAIL itemName: insert a new item with data = itemName as the tail of the linked list
    # POP_HEAD: delete the current head of the linked list
        # The dash at the right is a filler value since there is no itemName
# TODO: Return a reference to the head of the final linked list after applying all the queries
# NOTE: You are not allowed to use extra memory other than to create new nodes for queries PUSH_HEAD and PUSH_TAIL

# EXAMPLE:
    # head = pen -> cup
    # queries = [["PUSH_TAIL", "fan"], ["PUSH_HEAD", "jam"], ["POP_HEAD", "-"], ["POP_HEAD", "-"]]

    # Your initial shopping cart is: pen -> cup
    # In the 1st operation, you perform PUSH_TAIL fan
        # The new shopping cart is: pen -> cup -> fan
    # next, PUSH_HEAD jam
        # jam -> pen -> cup -> fan
    # next, POP_HEAD
        # pen -> cup -> fan
    # lastly, POP_HEAD -
        # return: cup -> fan

###########################################################################################################

# ✅ ALGORITHM:

def getShoppingCart(head, queries):
    if not head:
        tail = None # if head is null, tail is also null
    else:
        tail = head # initiate tail of LL to head
        while tail.next:
            tail = tail.next # keep iterating LL until we reach the last node -> this node is the tail

    for query in queries:
        op, item = query
        
        if op == "PUSH_HEAD":
            new_head = SinglyLinkedListNode(item)
            new_head.next = head
            head = new_head

            if not tail:
                tail = head # if tail is None, then this new head is the 1st node -> set tail to this head node
        
        elif op == "PUSH_TAIL":
            new_head = SinglyLinkedListNode(item)
            if tail is None:
                tail = head = new_head # new node is the new tail and head (it's the only node in LL)
            else:
                tail.next = new_head
                tail = new_head
        
        elif op == "POP_HEAD":
            if head:
                head = head.next

                if not head: # if head is null after popping previous head, set tail to null
                    tail = None
    
    return head