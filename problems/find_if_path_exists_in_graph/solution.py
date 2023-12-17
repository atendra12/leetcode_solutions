class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.graph = dict()
        self.flag = False
        self.vis = [False]*n

        ## edge cases
        if len(edges)==0:
            return source == destination
        
        for index in range(0,len(edges)):
            vertex_u, vertex_v= edges[index]
            ## need to add for both here
            ## before that how to check
            if vertex_u in self.graph: ## already exists append
                self.graph[vertex_u].append(vertex_v)
            else: ## create key and add one list element
                self.graph[vertex_u] = [vertex_v]
            if vertex_v in self.graph: ## already exists append
                self.graph[vertex_v].append(vertex_u)
            else: ## create key and add one list element
                self.graph[vertex_v] = [vertex_u]

        self.DFS(source,destination)
        return self.flag

    def DFS(self, source, destination):
        ## Enter vertex
        if self.flag:
            return 
        self.vis[source] = True
        for child in self.graph[source]:
            if child == destination:
                self.flag = True
                return 
            if self.vis[child]: 
                continue
            ## DO DFS on each child
            self.DFS(child,destination)
        ## take action on child after DFS
        ## take action on vertex before exit 
    



        



