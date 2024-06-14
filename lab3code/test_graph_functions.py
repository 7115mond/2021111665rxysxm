# test_graph_functions.py

import pytest
import networkx as nx
from graph_functions import rande_walk, traversed_nodes, traversed_edges, stop_traversal

def test_rande_walk():
    graph = nx.path_graph(5)  # 创建一个简单的路径图作为测试用例
    rande_walk(graph)
    
    assert traversed_nodes  # 检查是否有遍历到的节点
    assert traversed_edges  # 检查是否有遍历到的边

def test_stop_traversal():
    graph = nx.complete_graph(10)  # 创建一个完全图作为测试用例
    global stop_traversal
    
    stop_traversal = False
    rande_walk(graph)
    assert traversed_nodes
    
    stop_traversal = True
    rande_walk(graph)
    assert not traversed_nodes

if __name__ == "__main__":
    pytest.main()
