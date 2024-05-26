class Vertex:
    def __init__(self, name):
        self.name = name
        self.intree = 0 
        self.distance = float('inf')  
        self.parent = None 

class Graph:
    def __init__(self):
        self.vertices = {}  
        self.edges = [] 
        self.neighbours_dict = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges.append((u, v, weight))
            return True
        else:
            return False

    def neighbours(self, vertex_name):
        neighbours_list = []
        for u, v, weight in self.edges:
            if u == vertex_name:
                neighbours_list.append((v, weight))
            elif v == vertex_name:
                neighbours_list.append((u, weight))
        return neighbours_list

    def min_distance_vertex(self):
        min_distance = float('inf')
        min_vertex = None
        for vertex_name, vertex in self.vertices.items():
            if vertex.intree == 0 and vertex.distance < min_distance:
                min_distance = vertex.distance
                min_vertex = vertex
        return min_vertex

    
    def prim_mst(self, start_vertex_name):
        start_vertex = self.vertices[start_vertex_name]
        start_vertex.distance = 0
        total_weight = 0
        while True:
            current_vertex = self.min_distance_vertex()
            if current_vertex is None:
                break
            current_vertex.intree = 1

            for edge in self.edges:
                if edge[0] == current_vertex.name:
                    neighbor_vertex = self.vertices[edge[1]]
                elif edge[1] == current_vertex.name:
                    neighbor_vertex = self.vertices[edge[0]]
                else:
                    continue

                if neighbor_vertex.intree == 0 and edge[2] < neighbor_vertex.distance:
                    neighbor_vertex.parent = current_vertex.name
                    neighbor_vertex.distance = edge[2]

            if current_vertex.parent is not None:
                total_weight += current_vertex.distance

        mst = Graph()
        for vertex_name, vertex in self.vertices.items():
            if vertex.parent is not None:
                mst.add_vertex(Vertex(vertex.name))
                mst.add_vertex(Vertex(vertex.parent))
                mst.add_edge(vertex.parent, vertex.name, vertex.distance)
        return mst, total_weight

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices.values():
        print(v.name, end=" -> ")
        for (n, w) in g.neighbours(v.name):
            print(n, w, end="; ")
        print()
    print("-------------------")

if __name__ == "__main__":
    graf = [('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]
    
    graph = Graph()    
    for edge in graf:
        graph.add_vertex(Vertex(edge[0]))
        graph.add_vertex(Vertex(edge[1]))
        graph.add_edge(edge[0], edge[1], edge[2])
    
    print("Oryginalny Graf:")
    printGraph(graph)
    mst, total_weight = graph.prim_mst('A')
    print("\nMST:")
    printGraph(mst)
