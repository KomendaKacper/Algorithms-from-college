#Niedokończone
class Vertex:
    def __init__(self, key, ):
        self.key = key

    def __eq__(self, other):
        if self.key == other.key:
            return True
        
    def __hash__(self):
        return hash(self.key)
    
    def __str__(self):
        return str(self.key)

class Graph:
    def __init__(self):
            self.graph_dict = {}
            self.neighbours_dict = {}
            self.graph_list = []

    def __str__(self):
        res = ""
        for e in self.graph_dict:
            res += str(e) + ", "
        return res[:-2]
    
    # def __hash__(self):
    #     return hash(self.key)
    
    # def get_vertex(self, vertex_id):

    def is_empty(self):
        return self.graph_dict == {}
   
    def insert_vertex(self, vertex):
        self.graph_dict[vertex] = vertex
        self.neighbours_dict[vertex] = {}
        self.graph_list.append(vertex)

    # def insert_edge(self, vertex1, vertex2, edge):

    # def delete_vertex(self, vertex):

    # def delete_edge(self, vertex1, vertex2):

    def neighbours(self, vertex_id):
        return self.neighbours_dict[vertex_id]

    def vertices(self):
        return self.graph_dict



vertex = Vertex(5)
print (vertex)
graph = Graph()
graph.insert_vertex(vertex)
print (graph.is_empty())
print (graph)
print (graph.vertices())