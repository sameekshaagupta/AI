import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

def bfs(adj, s, G):
    q = deque()
    visited = [False] * len(adj)
    visited[s] = True
    q.append(s)
    
    print(f"Start BFS from vertex {s}.")
    
    while q:
        curr = q.popleft()
        print(f"Dequeued vertex: {curr}")

        # Highlight the visited node
        nx.draw(G, with_labels=True, node_color=['#00CFFF' if visited[i] else '#FF6347' for i in range(len(adj))], node_size=700, font_size=15, font_weight='bold')
        plt.title(f"BFS traversal - Visited node {curr}")
        plt.show()

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)
                print(f"Visited vertex {x}. Enqueued {x}.")
        
    print("BFS traversal completed.")

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]
    
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)
    
    print("Final adjacency list: ", adj)
    
    # Create a graph for visualization
    G = nx.Graph()
    for u in range(V):
        for v in adj[u]:
            G.add_edge(u, v)
    
    # Display the graph initially
    nx.draw(G, with_labels=True, node_size=700, font_size=15, font_weight='bold')
    plt.title("Graph Representation")
    plt.show()

    # Start BFS from vertex 0
    print("BFS starting from vertex 0: ")
    bfs(adj, 0, G)
