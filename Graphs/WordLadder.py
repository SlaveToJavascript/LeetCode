# https://leetcode.com/problems/word-ladder
# HARD
# Tags: bfslc, graphlc, #127

# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> endWord such that:
    # Every adjacent pair of words differs by a single letter
    # Every si and endWord is in wordList
        # Note that beginWord does not need to be in wordList
# TODO: Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists

# EXAMPLES:
    # Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    # Output: 5
    # Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

    # Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    # Output: 0
    # Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

###########################################################################################################

# ❌ ALGORITHM 1: NAIVE BFS
# Create an adjacency list 

# TIME COMPLEXITY: O(n^2 * m) ❌ (TLE)
    # n = no. of words in wordList
    # m = length of each word
    # O(n^2) for the nested for-loop to build adjacency list, multiplied by O(m) where we compare each character of the word

from collections import defaultdict

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    wordList.append(beginWord)    
    graph = defaultdict(set)
    for i in range(len(wordList)):
        if sum(wordList[i][x] != beginWord[x] for x in range(len(beginWord))) == 1:
            graph[beginWord].add(wordList[i])
        for j in range(i+1, len(wordList)):
            if sum(wordList[i][x] != wordList[j][x] for x in range(len(wordList[i]))) == 1:
                graph[wordList[i]].add(wordList[j])
                graph[wordList[j]].add(wordList[i])

    q = [(beginWord, 1)] # q[i] = (word, no. of changes)
    visited = set()
    visited.add(beginWord)

    while q:
        word, moves = q.pop(0)
        if word == endWord:
            return moves

        for w in graph[word]:
            # if w and word differs by 1 word, they have an edge
            if sum(w[i] != word[i] for i in range(len(word))) == 1 and w not in visited:
                q.append((w, moves+1))
                visited.add(w)
    
    return 0

#==========================================================================================================

# ✅ ALGORITHM 2: BFS WITH SPECIAL ADJACENCY LIST
# Since the above method gave TLE error, we create a more efficient adjacency list
# Since 2 words have an edge between each other if there is a 1-character difference, we can create an adjacency list where the key = a pattern with wildcard chars (e.g. "ca*"), and value = array of words that satisify this pattern
    # e.g. adjList["do*"] = ["dog", "dot", "doc"]
    # e.g. adjList["*og"] = ["dog", "cog", "log"]
    # notice that every word in each list differ from one another by 1 char
# When we're doing BFS, for each popped word, get every pattern that this popped word can satisfy and get its list of neighbors from the adjacency list using those patterns
# push those neighbors to the queue if they haven't been visited

# TIME COMPLEXITY: O(n^2 * m)
    # n = no. of words in wordList
    # m = length of each word
    # n > m (mostly)
    # O(n * m^2) for construction of adjacency list
    # O(n^2 * m) for BFS
        # there are n^2 edges -> BFS itself is n^2, but in each BFS operation we are iterating through all chars in the word -> O(n^2 * m)


from collections import defaultdict

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList: # if we cannot possibly reach endWord
        return 0
    
    wordList.append(beginWord) # add beginWord to wordList so that we can add its neighbors to adjList also
    adjList = defaultdict(set)
    for word in wordList:
        for i in range(len(word)): # i iterates through each char in word
            pattern = word[:i] + "*" + word[i+1:]
            adjList[pattern].add(word)
    
    q = [(beginWord, 1)] # from the examples, beginWord is also counted as part of the sequence -> start from 1
    visited = {beginWord}

    while q:
        word, moves = q.pop(0)
        if word == endWord:
            return moves
        
        for i in range(len(word)): # i iterates through each char in word
            pattern = word[:i] + "*" + word[i+1:]
            for neighbor in adjList[pattern]: # get all words that differ from popped word by 1 char
                if neighbor not in visited:
                    q.append((neighbor, moves+1))
                    visited.add(neighbor)
    
    return 0