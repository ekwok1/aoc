import sys
sys.path.insert(0, '../..')
from data_structures.directed_graph import DirectedGraph, EdgeFormat, GraphType
from utils.reader import read_lines

edges: list[str] = read_lines('./09.txt')

directed_graph: DirectedGraph = DirectedGraph(GraphType.TWO_WAY, EdgeFormat.WEIGHT_LAST, edges)
print(directed_graph.get_shortest_path())
