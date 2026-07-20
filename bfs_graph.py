""" Breadth-First Search (BFS) implementation for a graph represented as an adjacency list """


"""
is an adjacency list representation of a graph.

It means:

Node 0 is connected to 1 and 2.
Node 1 is connected to 3 and 4.
Node 2 has no outgoing edges.
Node 3 has no outgoing edges.
Node 4 is connected to 0.
"""



class solution():
      def bfs(self,adj,start):
        visited=[False] * len(adj)
        levels=[-1] * len(adj)     #not required for dfs
        parent=[-1] * len(adj)    #not required for dfs
        queue=[]                 #use stack


        i=1                     #not for dfs
        queue.append(start)         # use stack
        visited[start]=True
        levels[start]=i-1                 #not for dfs
        parent[start]=-1                 #not for dfs

        while queue:
              u=queue[0]                        # where u=stack[-1]
              print(u,end='->')      
              del(queue[0])                   #delete stack[-1]
              for v in adj[u]:
                  if not visited[v]:
                      queue.append(v)
                      visited[v]=True
                      parent[v]=u     #not for dfs  #use this for shortest path
                      levels[v]=i       #not for dfs
              i+=1

if __name__=="__main__":
    adj=[[1,2],[3,4],[],[],[0]]   #create adjacency if edges given
    start=0
    s=solution()
    print(s.bfs(adj,start))
    #print(s.bfs(adj,1))