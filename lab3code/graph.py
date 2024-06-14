import matplotlib.pyplot as plt  # 导入 Matplotlib 工具包
import networkx as nx  # 导入 NetworkX 工具包
from txt_despose import *
import random
import signal
import sys
def show(graph):
    G2 = nx.DiGraph()
    for x in graph:

        G2.add_edge(x['pre'], x['bhd'], weight=x['weight'])
    pos = nx.spring_layout(G2)  # 用 FR算法排列节点
    nx.draw(G2, pos, with_labels=True, alpha=0.5)
    labels = nx.get_edge_attributes(G2, 'weight')
    nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels)
    plt.show()

def pre_process(file_name):
    with open(file_name) as file_object:
        contents = file_object.read()
    contents = replace_punctuation_with_whitespace(contents)
    words = contents.split()
    g = []
    node = {'pre':words[0],'bhd':words[1],'weight':1}
    g.append(node)
    lens = len(words)  
    i=1
    while i<lens-1:
        pre = words[i]
        bhd = words[i+1]
        i=i+1
        weight =1
        node = {'pre':pre,'bhd':bhd,'weight':weight}
        a=0
        j=0
        while j<len(g):
            if pre == g[j]['pre'] and bhd == g[j]['bhd']:
                g[j]['weight'] = g[j]['weight']+1
                a=1
            j=j+1
        if a==1:
            continue
        else:
            g.append(node)
    return g

def find_bridge(words, word_1, word_2):
    i = 0
    j = 0
    lax = 0
    num = 0
    test = []
    bridge = []
    for node in words:
        test.append(node['pre'])
    if word_1 in test and word_2 in test:
        while i < len(words):
            if word_1 == words[i]['pre']:
                while j < len(words):
                    if j != i and words[j]['bhd'] == word_2 and words[i]['bhd'] == words[j]['pre']:
                        bridge.append(words[j]['pre'])
                        num = num + 1
                        lax = 1
                    j = j + 1
            j = 0
            i = i + 1
    else:
        return 'No word1 or word2 in the graph'
    if lax == 0:
        return 'No bridge words from word1 to word2!'
    if num == 1:
        return f'The bridge word from {word_1} to {word_2} is {bridge[0]}'
    if num > 1:
        return f'The bridge words from {word_1} to {word_2} are {", ".join(bridge)}.'


def sperate(file_name):
    with open(file_name) as file_object:
        contents = file_object.read()
    contents = replace_punctuation_with_whitespace(contents)
    words = contents.split()
    return words

def txt_make(file_name,words):
    words_new = sperate(file_name)
    i=0
    words_change=[]
    words_change.append(words_new[0])
    while i < len(words_new)-1:
        if get_bridge(words,words_new[i],words_new[i+1]):
            words_change.append(get_bridge(words,words_new[i],words_new[i+1])[0])
        words_change.append(words_new[i+1])
        i=i+1
    return words_change

def min_way(graph,word_1,word_2):
    G2 = nx.DiGraph()
    for x in graph:
        G2.add_edge(x['pre'], x['bhd'], weight=x['weight'])
        
    minWPath_w1_w2 = nx.dijkstra_path(G2, source=word_1, target=word_2)
    lMinWPath_w1_w2 = nx.dijkstra_path_length(G2, source=word_1, target=word_2)
    print('The minest weight of way from '+word_1+' to '+word_2+' is '+str(lMinWPath_w1_w2))
    pos = nx.spring_layout(G2)  # 用 FR算法排列节点
    nx.draw(G2, pos, with_labels=True, alpha=0.5)
    labels = nx.get_edge_attributes(G2, 'weight')
    nx.draw_networkx_edge_labels(G2, pos, edge_labels=labels)
    #plt.show()
    edgeList = []
    for i in range(len(minWPath_w1_w2)-1):
        edgeList.append((minWPath_w1_w2[i], minWPath_w1_w2[i+1]))
    nx.draw_networkx_edges(G2, pos, edgelist=edgeList, edge_color='m', width=4)  # 设置边的颜色
    plt.show() 

def signal_handler(sig, frame):
    global stop_traversal
    stop_traversal = True
    print("\nTraversal stopped by user.")

traversed_nodes = []
traversed_edges = set()
stop_traversal = False

def random_traversal(graph):
    global stop_traversal
    start_node = random.choice(list(graph.nodes))
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
    G2 = nx.DiGraph()
    for x in graph:

        G2.add_edge(x['pre'], x['bhd'], weight=x['weight'])
    signal.signal(signal.SIGINT, signal_handler)
    random_traversal(G2)
    output_text = " -> ".join(traversed_nodes)
    output_filename = "traversed_nodes.txt"
    with open(output_filename, "w") as file:
        file.write(output_text)
    print(f"Traversal complete. Nodes traversed: {output_text}")
    print(f"Output written to {output_filename}")


words = pre_process('text.txt')
print(find_bridge(words,'our','life'))
#print(txt_make('text_insert.txt',words))
#min_way(words,'out','and')
#rande_walk(words)




#show(words)



