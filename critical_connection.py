"""Critical Connection
Given a network of n servers connected by undirected server-to-server connections, identify all the critical connections in the network. A critical connection is defined as a connection that, if removed, would result in some servers being unable to reach other servers.

Definitions:

Servers are numbered from 0ton - 1.
Connections are represented by pairs of integers [ai, bi], indicating a bidirectional connection between servers aiandbi.
A server can reach another server if there is a path of connections from one to the other.
Input Format:

The first line contains two space-separated integers nandm, where nis the number of servers andm is the number of connections.
The next m lines each contain two space-separated integers representing a connection between two servers.
Output Format:

Print the critical connections in any order. Each critical connection should be printed as two space-separated integers per line.
If there are no critical connections, print -1.
Sample Input:

7 8
6 1
4 2
2 5
1 5
0 1
1 2
2 0
1 3
Sample Output:

1 6
2 4
1 3
Constraints:

2 <= n <= 10^5
n - 1 <= connections.length <= 10^5
0 <= ai, bi <= n - 1
ai != bi
Connections are unique and undirected.
Explanation: In this example, the network consists of 7 servers and 8 connections. The critical connections are between servers 1-6, 2-4, and 1-3. Removing any of these connections would result in at least one server being isolated from the rest of the network.
"""



# Python code for the above approach:
def dfs(i, p, rank, k, adj, ans, vis):

	# Set rank of the ith node to k
	# which is depth
	rank[i] = k

	# Mark ith node as visited
	vis[i] = 1

	min_depth = float('inf')

	# Exploring all the neighbour
	# node of node i
	for ch in adj[i]:

		# This if condition is to make
		# sure we do not call parent
		# from where it is called to
		# avoid child parent loop
		if ch != p:

			# If neighbour is already
			# visited then we take
			# minimum with rank of ch,
			# means a cycle is found
			if vis[ch]:
				min_depth = min(min_depth, rank[ch])

			# If neighbour is not
			# visited then we go in
			# depth to check cycle
			# is present or not
			else:
				min_rank = dfs(ch, i, rank, k + 1, adj,
							ans, vis)

				# If dfs returns smaller
				# depth value than current
				# depth it means current
				# edge is in a cycle
				# else there is no cycle
				# so we have pushed the
				# edge in our answer
				if rank[i] < min_rank:
					ans.append([i, ch])
				min_depth = min(min_rank, min_depth)
	return min_depth

# Function to calculate
# the critical edges


def critical_connections(V, adj):
	ans = []
	rank = [-1] * V
	vis = [0] * V
	dfs(0, -1, rank, 0, adj, ans, vis)
	for i in range(len(ans)):
		ans[i].sort()
	ans.sort()
	return ans


# Drivers code
v = 3
e = 2
edges = [[0, 1], [0, 2]]
adj = [[] for _ in range(v)]
for i in range(e):
	adj[edges[i][0]].append(edges[i][1])
	adj[edges[i][1]].append(edges[i][0])
ans = critical_connections(v, adj)
ans.sort()
for i in range(len(ans)):
	print(ans[i][0], ans[i][1])

# This code is contributed by Tapesh(tapeshdua420)


