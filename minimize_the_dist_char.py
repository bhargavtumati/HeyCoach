"""
Minimize the Number of distinct Character in the path
Given a MST with N vertices numbered 1, 2, ..., N, and N-1 edges connecting these vertices with weights w1, w2, ..., wN-1, define the function f(u, v) as the Smallest weight of an edge contained in the shortest path from Vertex u to Vertex v. How can you efficiently compute or find the values of f(u, v) for all pairs of vertices u and v in the given tree?

The given graph is a MST.

All values in input are integers.

Input:

First Line Contains the Positive Number N Then N-1 lines containing u,v vertex with given edge weight w.

Output:

Print the Sum of all f(u, v) over all possible pairs where u!=v.

Sample Input1
5

1 2 5

2 3 10

4 2 3

3 5 20
Output
67
Sample Input 2
5

1 2 1

2 3 2

4 2 5

3 5 14
Output
31
Constraints:
2 ≤ N ≤ 10^5

1 ≤ u[i],v[i] ≤ N

1 ≤ w[i] ≤ 10^7
"""