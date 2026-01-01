#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#

def countGroups(related):
    #adjacency list dfs traversal of the graph to find number of disconnected componenets
    n = len(related)
    vis = [0] * n
    # dfs APPROACH
    def dfs(node):
        for i in range(n):
            if related[node][i] == '1' and not vis[i]: # node is connected
                vis[i]=1
                dfs(i)
    num_groups = 0
    for i in range(n):
        if not vis[i]: # every not visited node is a disconnected node or cluster
            num_groups+=1
            dfs(i)
    return num_groups # number of dfs required to traverse the entire graph
        
    
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    related_count = int(input().strip())

    related = []

    for _ in range(related_count):
        related_item = input()
        related.append(related_item)

    result = countGroups(related)

    fptr.write(str(result) + '\n')

    fptr.close()

