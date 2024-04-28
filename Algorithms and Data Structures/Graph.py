import polska

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if self.key == other.key:
            return True
        
    def __hash__(self):
        return hash(self.key)
    
    def __str__(self):
        return str(self.key)
    
    def __repr__(self):
        return repr(self.key)

class ListGraph:
    def __init__(self):
        self.graph_dict = {}
        self.neighbours_dict = {}

    def is_empty(self):
        return self.graph_dict == {}

    def insert_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = vertex
            self.neighbours_dict[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        self.neighbours_dict[vertex1][vertex2] = edge
        self.neighbours_dict[vertex2][vertex1] = edge

    def get_vertex(self, vertex_id):
        return self.graph_dict.get(vertex_id)
    
    def get_vertex_id(self, vertex):
        return vertex

    def delete_vertex(self, vertex):
        del self.neighbours_dict[vertex]
        del self.graph_dict[vertex]
        for neighbours in self.neighbours_dict.values():
            neighbours.pop(vertex, None)

    def delete_edge(self, vertex1, vertex2):
        del self.neighbours_dict[vertex1][vertex2]
        del self.neighbours_dict[vertex2][vertex1]

    def neighbours(self, vertex_id):
        return self.neighbours_dict.get(vertex_id, {}).items()

    def vertices(self):
        return self.graph_dict.keys()

class MatrixGraph:
    def __init__(self, val=0):
        self.graph_list = []
        self.neighbours_matrix = []
        self.val = val

    def get_vertex_id(self, vertex):
        for i in range(len(self.graph_list)):
            if self.graph_list[i] == vertex:
                return i
        return None
    
    def get_vertex(self, vertex_id):
        return self.graph_list[vertex_id]
    
    def is_empty(self):
        return self.graph_list == []
    
    def insert_vertex(self, vertex):
        if vertex not in self.graph_list:
            self.graph_list.append(vertex)
            size = len(self.graph_list)
            for row in self.neighbours_matrix:
                row.append(self.val)
            self.neighbours_matrix.append([self.val] * size)

    def insert_edge(self, vertex1, vertex2, edge=1):
        idx1 = self.get_vertex_id(vertex1)
        idx2 = self.get_vertex_id(vertex2)
        
        self.neighbours_matrix[idx1][idx2] = edge
        self.neighbours_matrix[idx2][idx1] = edge

    def delete_vertex(self, vertex):
        idx = self.get_vertex_id(vertex)
        if idx is not None:
            del self.graph_list[idx]
            del self.neighbours_matrix[idx]
            for row in self.neighbours_matrix:
                del row[idx]
    
    def delete_edge(self, vertex1, vertex2):
        idx1 = self.get_vertex_id(vertex1)
        idx2 = self.get_vertex_id(vertex2)
    
        if idx1 != None and idx2 != None:
            self.neighbours_matrix[idx1][idx2] = self.val
            self.neighbours_matrix[idx2][idx1] = self.val
            
    def __str__(self):
        res = ""
        for e in self.graph_list:
            res += str(e) + ", "
        return res[:-2]
    
    def neighbours(self, vertex_id, edge = 1):
        res = []
        for idx, vertex in enumerate(self.neighbours_matrix[vertex_id]):
            if vertex != 0:
                res.append((idx, edge))
        return res

    def vertices(self):
        res = []
        for i in range(len(self.graph_list)):
            res.append(i)
        return res

edges = polska.graf
pol=polska.polska
vertices = []

for e in edges:
    if Vertex(e[0]) not in vertices:
        vertices.append(Vertex(e[0]))
    if Vertex(e[1]) not in vertices:
        vertices.append(Vertex(e[1]))

list_graph = ListGraph()
matrix_graph = MatrixGraph()

for vertex in vertices:
    list_graph.insert_vertex(vertex)
    matrix_graph.insert_vertex(vertex)

for edge in edges:
    v1 = Vertex(edge[0])
    v2 = Vertex(edge[1]) 
    list_graph.insert_edge(v1, v2)
    matrix_graph.insert_edge(v1, v2)

list_graph.delete_vertex(Vertex('K'))
matrix_graph.delete_vertex(Vertex('K'))

list_graph.delete_edge(Vertex('W'), Vertex('E'))
matrix_graph.delete_edge(Vertex('W'), Vertex('E'))

pol = [(e[2], e[2]) for e in pol if Vertex(e[2]) in list_graph.vertices()]

polska.draw_map(list_graph, pol)
polska.draw_map(matrix_graph, pol)
