# https://leetcode.com/problems/minimum-genetic-mutation/description
# MEDIUM
# Tags: bfslc, #433

# A gene string can be represented by an 8-character string, where each char in ('A', 'C', 'G', 'T')
# 1 mutation = 1 char changed in the string
    # e.g. "AACCGGTT" --> "AACCGGTA" = 1 mutation
# There is also a gene bank bank that records all the valid gene mutations (if a gene obtained after a mutation is not in gene bank, it is not a valid mutation)
    # A gene must be in bank to make it a valid gene string
# Given the two gene strings startGene and endGene and the gene bank, return the minimum number of mutations needed to mutate startGene to become endGene
    # If there is no such a mutation, return -1

# EXAMPLES:
    # Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
    # Output: 1

    # Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    # Output: 2

###########################################################################################################

# ✅ ALGORITHM: BFS
# Each valid gene string is a node, and each gene string (node) A has an edge with another gene string (another node) B if gene string A can be mutated into valid gene string B
# For each gene string A, we obtain all possible neighbors of A (i.e. valid gene strings that are mutated from A) by iterating through each char in gene string A and replacing it with each possible char (A/G/T/C)
    # when we find a valid neighbor, we push it into the queue
# when we pop a gene string from the queue which is = endGene, return the no. of mutations taken for it to reach the current gene string

# TIME COMPLEXITY: O(N * 4^8) = O(N) where N = no. of genes in bank
    # O(N) to iterate through each gene in bank
    # O(4^8) to iterate through each char in each gene string
# SPACE COMPLEXITY: O(N) where N = no. of genes in bank
    # O(N) to store all genes in bank
    # O(N) to store all genes in queue

def minMutation(startGene, endGene, bank):
    q = [(startGene, 0)] # q[i] = (gene string, no. of mutations to get from startGene to popped gene)
    visited = set()

    while q:
        gene, mutations = q.pop(0)
        if gene == endGene: # if popped gene is endGene,
            return mutations # return no. of mutations taken from startGene to get to current gene

        for i in range(len(gene)): # for each char in gene,
            for char in "ACGT": # try replacing it with each possible char
                neighbor = gene[:i] + char + gene[i+1:] # get a mutated gene

                if neighbor not in visited and neighbor in bank: # if mutated gene is a valid gene,
                    q.append((neighbor, mutations+1)) # neighbor is a valid neighbor -> add to queue
                    visited.add(neighbor) # mark as visited
    
    return -1