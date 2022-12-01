import sys
sys.path.insert(0, '../..')
from data_structures.directed_graph import DirectedGraph, EdgeFormat, GraphType
from utils.reader import read_lines

edges: list[str] = read_lines('./13.txt')

directed_graph: DirectedGraph = DirectedGraph(GraphType.ONE_WAY, EdgeFormat.WEIGHT_MIDDLE, edges)
print(directed_graph.get_longest_round_trip(two_way=True))
