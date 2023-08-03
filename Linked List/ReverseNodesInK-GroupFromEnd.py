# SIMILAR TO BUT SLIGHTLY DIFFERENT FROM https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# HARD
# Tags: linkedlistlc, #25, Reverse Nodes in k-Group, ReverseNodesinkGroup

# GIVEN:
    # head of a linked list, head
    # positive integer, k, which is less than or equal to the length of the linked list

# TASK:
    # reverse the nodes of the list k at a time from THE END OF THE LL, and return modified list

# EXAMPLES:
    # Input: head = [1,2,3,4,5], k = 2
    # Output: [1, 3, 2, 5, 4]

    # Input: head = [1,2,3,4,5], k = 3
    # Output: [1, 2, 5, 4, 3]

    # Input: head = [1,2,3,4,5,6,7,8,9], k = 4
    # Output: [1,5,4,3,2,9,8,7,6]

###########################################################################################################

# ✅ ALGORITHM 1
# Main idea: 
    # 1. reverse entire linked list 
    # 2. get every k-chunk of the reversed list,
    # 3. for each chunk, keep track of groupPrev (the starting node of the previous chunk) as groupPrev will be chained behind this current chunk, and keep track of groupNext (the node after the current chunk) as groupNext will be the starting node of the next chunk
    # 4. for every k-chunk, chain the last node of the chunk to the first node of the previous chunk (or chain to null if the current k-chunk is the first we've processed)
    # 5. any remaining chunks with length < k will be chained to the front of the resulting linked list

# e.g. 
    # 1. [1,2,3,4,5] -> reverse -> [5,4,3,2,1]
    # 2. first k-chunk = [5,4]
    # 3. groupPrev = null (since we are currently at the 1st chunk so this 1st chunk will become the last chunk in the resulting linked list -> therefore it should point to null), groupNext = 3 (3 is the node after chunk [5,4])
    # 4. Change 4's next pointer to point to groupPrev (which is null here)
    # 4a. Update groupPrev with 5 (the starting node of the current chunk) -> this updated groupPrev value is to be used for the next chunk i.e. [3,2]
        # this is because the next chunk, [3,2], is to be chained in front of 5 in the resulting LL
    # 4b. To iterate to the next chunk, update chunkStart = groupNext (i.e. 3), as groupNext represents the node that came after our previous chunk [5,4] -> now it will be the first node of our next chunk [3,4]
    # 5. After the iteration, chunkStart will be the node that comes after the last k-chunk (chunkStart will be null if there are no more remaining nodes after the last k-chunk i.e. if length of the linked list is a multiple of k)
    # 5a. If chunkStart is not null (i.e. there are remaining nodes after the last k-chunk), we iterate to the tail of the last non-k chunk, and chain the last node of this non-k chunk to groupPrev (since groupPrev is the 1st node of the last chunk that we processed) -> return chunkStart
    # 5b. If chunkStart is null (i.e. there are no more remaining nodes after the last k-chunk) -> return groupPrev (i.e. the 1st node of the last chunk we processed)

# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(1)

def reverseKGroupFromEnd(head, k):
    def getChunkEnd(curr, k): # get the ending node of a k-chunk whose starting node is curr
        # e.g. [1,2,3], curr=2, k=2 -> return node 3 (the k-chunk here would be [2,3])
        while curr and k > 1: # it's k>1 and not k>0 as it takes k-1 jumps from starting node of k-chunk to reach ending node of k-chunk
            curr = curr.next
            k -= 1
        return curr
    
    # Reverse entire linked list
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # at this point, the starting node of the reversed LL would be prev
    # i.e. prev = [5,4,3,2,1]

    # Iterate LL to get the next k-chunks
    groupPrev = None # initialize groupPrev to null as the first k-chunk we process will end up as the last chunk in the resulting array -> null will be chained behind it
    chunkStart = prev # chunkStart is the starting node in the current k-chunk

    while True:
        chunkEnd = getChunkEnd(chunkStart, k) # chunkEnd is the ending node of current k-chunk
        if not chunkEnd: break # if chunkEnd is null, it means we are dealing with the last chunk of our LL and this group is not even big enough for us to reverse it (i.e. it's not a k-chunk)
            # e.g. 1 -> 2 -> null and k = 3 -> chunkEnd is null node as the remaining chunk size is 2 i.e. chunk [1,2]
        
        # if current chunk = [5,4],
        groupNext = chunkEnd.next # groupNext is the element after the current chunk
            # i.e. groupNext = 3
        chunkEnd.next = groupPrev # i.e. ... -> 4 -> null
        groupPrev = chunkStart # i.e. groupPrev = 5 -> this would be the node that will be chained behind the next k-chunk, [3,2]
        chunkStart = groupNext # i.e. chunkStart = 3 -> 3 is the node behind our current k-chunk and 3 will become the starting node of our next k-chunk from our next iteration

    if chunkStart: # if there are remaining nodes after our last possible k-chunk,
        curr = chunkStart
        while curr: # we iterate the remanining nodes to get to the last remainining node
            tail = curr
            curr = curr.next
        tail.next = groupPrev # chain the last remaining node to groupPrev (since groupPrev is the 1st node of the last chunk that we processed) i.e. groupPrev = 3
        # in the above line, we chain 1 -> 3 -> ...
    else: # if there are no remaining nodes after our last possible k-chunk (i.e. length(LL) is multiple of k)
        chunkStart = groupPrev # we can either return groupPrev directly or use the chunkStart var to standardize the return statement

    return chunkStart