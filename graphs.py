import math
from collections import defaultdict
import graphviz
infinity = float('inf')

def visualise_weighted_graph(G, W):
    dot = graphviz.Graph()
    dot.attr(rankdir='LR')
    for name in G.keys():
        dot.node(name)
    for (u, v), w in W.items():
        if u < v:
            dot.edge(u, v, label=str(w))
    return dot

G = defaultdict(list)
W = {}
nodes = [x for x in range(2, 51)]
def design_graph():
    for i in nodes: 
        for j in nodes: 
            if i != j:
                if math.gcd(i, j) > 1:
                    G[i].append(j)
                    G[j].append(i)
                    W[i, j] = W[j, i] = 1/math.gcd(i,j)
                else: 
                    W[i,j] = infinity
                
    return G, W

start = 9
predecessor = {start: None}
q = {start: 0}
shortest = {}

def djikstra(G, W, destination_node):
        while q:
            
            '''
            NEED TO ADD IF 2 EDGES HAVE THE SAME WEIGHT, COMPUTE BOTH PATH AND CHOOSE BEST ONE WHEN THEY ARE DIFFERENT
            '''
            my_canditates = [(d, vertex) for vertex, d in q.items()]
            d, vertex = min((d, vertex) for vertex, d in q.items())
            if my_canditates[0] != 0:
                for i in range(len(my_canditates)):
                    if (my_canditates[i][0] == d):
                        d, vertex = my_canditates[i][0], my_canditates[i][1]

                del q[vertex]
                shortest[vertex] = d
                
                if vertex == destination_node:
                    return predecessor, shortest

                for next_vertex in G[vertex]:
                    if next_vertex in shortest:
                        continue
                    c = q.get(next_vertex, infinity)
                    e = d+W[vertex, next_vertex]
                    if e < c:
                        q[next_vertex] = e
                        predecessor[next_vertex] = vertex
                    
        return predecessor, shortest

def get_shortest_distance(start_node, end_node):
    destination = end_node
    G, W = design_graph()
    predecessor, shortest = djikstra(G, W, end_node)
    print(end_node)
    while True:
        previous_node = predecessor[end_node]
        print('^')
        print('|')
        print(previous_node)
        if previous_node == start_node:
            return 'Shortest distance found is: ' + str(shortest[destination])
        end_node = previous_node


print(get_shortest_distance(9, 50))

