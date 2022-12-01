import sys
sys.path.insert(0, '../..')
from data_structures.directed_graph import DirectedGraph, EdgeFormat, GraphType
from utils.reader import read_lines

edges: list[str] = read_lines('./13.txt')

directed_graph: DirectedGraph = DirectedGraph(GraphType.ONE_WAY, EdgeFormat.WEIGHT_MIDDLE, edges)
directed_graph.add_vertex('Me')
for vertex in directed_graph.vertices:
  directed_graph.add_edge('Me', vertex, 0)
  directed_graph.add_edge(vertex, 'Me', 0)
print(directed_graph.get_longest_round_trip(two_way=True))
