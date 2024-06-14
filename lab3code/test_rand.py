import networkx as nx
from gtaph_t import rande_walk

def test_empty_graph():
    # Create an empty graph
    graph = nx.DiGraph()    
    print("Testing empty graph:")
    rande_walk(graph)
    
def test_small_graph():
    # Create a small graph
    graph = nx.DiGraph()
    graph.add_edges_from([
        ('a', 'b', {'weight': 1}),
        ('b', 'c', {'weight': 1}),
        ('c', 'd', {'weight': 1}),
        ('d', 'e', {'weight': 1}),
        ('e', 'f', {'weight': 1}),
        ('f', 'g', {'weight': 1}),
    ])
    
    print("\nTesting small graph:")
    rande_walk(graph)
    
if __name__ == "__main__":
    test_empty_graph()
    test_small_graph()
