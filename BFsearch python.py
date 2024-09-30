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
        
    def bfsearch(self,start_node) :  
        #starting node to be chosen from any nodes       
        queue=[start_node]   

        #initialize empty list of visited nodes 
        visited=[]                      
        bfs_order=[]
        while queue:
            node=queue.pop(0)
            if node not in visited : 
                #appends unvisited nodes to the visited  list     
                visited.append(node) 

                #updates the order of breadth first search   
                bfs_order.append(node) 

                for neighbour in self.graph[node]:
                    if neighbour not in visited:      
                        queue.append(neighbour) 
        return bfs_order
g=Graph()
g.addedge('a','b')
g.addedge('a','c')
g.addedge('a','d')
g.addedge('b','a')
g.addedge('c','a')
g.addedge('d','c')
g.addedge('b','d')
g.addedge('d','a')

print(g.bfsearch("a"))