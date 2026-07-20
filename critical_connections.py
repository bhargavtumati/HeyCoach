
"""

Code


Testcase
Testcase
Test Result
1192. Critical Connections in a Network
Solved
Hard
Topics
Companies
Hint
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
234.3K
Submissions
418.2K
Acceptance Rate
56.0%
Topics
Companies
Hint 1
Use Tarjan's algorithm."""


from typing import List


class Solution:
   
    def dfs(self, graph, src, visited,parent, disc, low,time,ans):
        visited[src] = True              # The dfs method performs a depth-first search (DFS) to find critical connections. 
        disc[src]=time                   # It maintains arrays for discovery time (disc), low time (low), and visited nodes (visited).
        low[src]=time                    # The key idea is to identify bridges (critical connections) in the graph.

        for nbr in graph[src]:
            if parent==nbr:
                continue
            elif visited[nbr]:
                low[src] = min(low[src],disc[nbr])
            else:
                self.dfs(graph,nbr,visited,src,disc,low,time+1,ans)
                low[src] = min(low[src],low[nbr])

                if low[nbr]>disc[src]:
                    ans.append((src,nbr))

    def critical_connections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for v in range(n)]

        for connection in connections:
            src, des = connection[0],connection[1]       # The criticalConnections function initializes the graph and then calls the dfs method 
            graph[src].append(des)                       # starting from node 0. It collects critical connections (bridges) and 
            graph[des].append(src)                       # returns them as a list of pairs.
        
        ans = []
        self.dfs(graph,0,[False]*n,-1,[0]*n,[0]*n,0,ans)

        return ans

if __name__=="__main__":
    connections=[[0,1],[1,2],[2,0],[1,3]]
    n=4
    s=Solution()
    print(s.critical_connections(n,connections))

