"""
Converging maze: largest sum cycle
You are given a maze with N cells. Each cell may have multiple entry points but not more than one exit.(i.e. entry/exit points are unidirectional doors like valves).
The cells are named with an integer value from zero to N-1.
You have to find :
The sum of the largest sum cycle in the maze. Return -1 if they are no cycles.
	1. Sum of a cycle is the sum of the node number of all nodes in that cycle.
 input format 
	1. the first line has the number of cells N 
	2. The second line as the list of N values of the edge[] array. edge[i] contains cell number that can be reached from the cell 'i' in one step. Edge[i] is -1 if the 'I'th cell doesn't have an exit.

Output format:
The first line denotes the sum of the largest sum cycle.

Sample input and output
Input:
1  # no of test cases
23
4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 22 21 
Output:
45
"""




from typing import List

v = [] #graph adjacency
vis = []  # check if visited
par = []  # parent nodes
tmp = []  #tmp list to store current path


def dfs(node: int, p: int = -1) -> int:  #if it encounters a back edge (alrady visited), it calculates the sum of the cycle and returns it
    vis[node] = 1
    par[node] = p
    tmp.append(node)
    for i in v[node]:
        if vis[i] == 0:
            z = dfs(i, node)
            if z != -1:
                return z
        elif vis[i] == 1:
            sum = i
            while node != i:
                sum += node
                node = par[node]
                if node == i:
                    return sum
            return -1
    return -1


def largestSumCycle(N: int, Edge: List[int]) -> int:                         #The main part of the code iterates through all nodes (from 0 to N-1)
    ans = -1                                                 # For each unvisited node, it calls dfs to explore the graph.
    global v, vis, par, tmp                        # The maximum sum of any cycle encountered so far is updated in the ans variable.
    vis = [0] * N                                      #visited [0,0,0....]
    v = [[] for _ in range(N)]                            #v=[[],[],[],....]
    par = [-1] * N                                    #par=[-1,-1,-1,...]
    for i in range(N):
        if Edge[i] != -1:
            v[i].append(Edge[i])                       #[[1,2,3],[],...]

    for i in range(N):
        if not vis[i]:
            ans = max(ans, dfs(i))
            for j in tmp:
                vis[j] = 2
            tmp.clear()

    return ans


# Driver code
if __name__ == '__main__':
    testcases = 1
    N = 23
    Edge = [4, 4, 1, 4, 13, 8, 8, 8 ,0 ,8 ,14, 9 ,15, 11, -1 ,10, 15, 22, 22, 22, 22, 22, 22, 21]
    # Function Call
    ans = largestSumCycle(N, Edge)
    print(ans)


