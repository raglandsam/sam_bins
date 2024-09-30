class Graph :
    def __init__(self):
        self.graph={}
        self.directed = False 

    def addvertex(self,vertex) :
        if vertex not in self.graph :
            self.graph[vertex]=[]

    def addedge(self,sou,dest):
        self.addvertex(sou)              #if source vertex aint present in the vertex list
        self.addvertex(dest)             #if destination vertex aint present in the vertex list
        
        #if its a directed graph
        self.graph[sou].append(dest)
        
        #if its undirected 
        if self.directed==True:
            self.graph[dest].append(sou)

    def dfsearch(self,node):
        stack = [node]           # Use a stack for DFS (LIFO)
        visited = []                   # List to store visited nodes
        dfs_order = []                 #list to store the dfs traversal order 
        while stack :  
            node =stack.pop()             
            if node not in visited :
                visited.append(node)
                dfs_order.append(node)

                for neighbour in reversed(self.graph[node]): # Reverse to maintain correct order
                    if neighbour not in visited:
                         stack.append(neighbour)
        
        return dfs_order
g=Graph()
g.addedge('a','b')
g.addedge('a','c')
g.addedge('a','d')
g.addedge('b','a')
g.addedge('c','a')
g.addedge('d','c')
g.addedge('b','d')
g.addedge('d','a')

print(g.dfsearch('a'))
