class Solution:
    def check(self, n, m, edges): 
        #code here
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        def solve(cur, graph, vis, n):
            if sum(vis)==n: return True
            for neigh in graph[cur]:
                if vis[neigh]==0:
                    vis[neigh] = 1
                    if solve(neigh, graph, vis, n): return True
                    vis[neigh] = 0
            return False
        vis = [0] * n
        for i in range(n):
            vis[i] = 1
            if solve(i, graph, vis, n): return True
            vis[i] = 0
            return False
