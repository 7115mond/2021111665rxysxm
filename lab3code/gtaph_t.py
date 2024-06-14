import matplotlib.pyplot as plt
import networkx as nx
import random
import signal
import sys

def random_traversal(graph):
    global stop_traversal
    try:
        start_node = random.choice(list(graph.nodes))
    except IndexError:
        print("Error: Graph is empty or does not contain any nodes.")
        return
    
    current_node = start_node
    traversed_nodes.append(current_node)
    
    while True:
        if stop_traversal:
            break

        neighbors = list(graph.successors(current_node))
        
        if not neighbors:
            break
        
        next_node = random.choice(neighbors)
        edge = (current_node, next_node)
        
        if edge in traversed_edges:
            break
        
        traversed_nodes.append(next_node)
        traversed_edges.add(edge)
        current_node = next_node

def rande_walk(graph):
    signal.signal(signal.SIGINT, signal_handler)
    random_traversal(graph)
    
    if traversed_nodes:
        output_text = " -> ".join(traversed_nodes)
        output_filename = "traversed_nodes.txt"
        with open(output_filename, "w") as file:
            file.write(output_text)
        print(f"Traversal complete. Nodes traversed: {output_text}")
        print(f"Output written to {output_filename}")
    else:
        print("Traversal failed. No nodes were traversed.")

def signal_handler(sig, frame):
    global stop_traversal
    stop_traversal = True
    print("\nTraversal stopped by user.")

traversed_nodes = []
traversed_edges = set()
stop_traversal = False
