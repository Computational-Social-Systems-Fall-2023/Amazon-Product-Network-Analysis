import networkx as nx

# Step 1: Read the graph from the text file
# Replace 'your_graph.txt' with the path to your graph file
with open('com-amazon.ungraph.txt', 'r') as file:
    lines = file.read().splitlines()

# Create an empty undirected graph
G = nx.Graph()

# Parse and add edges to the graph
for line in lines:
    if not line.strip().startswith("#"):  # Ignore empty lines
        source, target = map(int, line.split())  # Assuming the file contains two integers per line
        G.add_edge(source, target)

# Number of Nodes
num_nodes = G.number_of_nodes()

# Number of Edges
num_edges = G.number_of_edges()

# Average Degree
average_degree = (2 * num_edges) / num_nodes if num_nodes > 0 else 0

print("Number of Nodes:", num_nodes)
print("Number of Edges:", num_edges)
print("Average Degree:", average_degree)

# Identify connected components in the graph
connected_components = list(nx.connected_components(G))

# Find the largest connected component
largest_component = max(connected_components, key=len)

# Create a subgraph from the largest connected component
largest_subgraph = G.subgraph(largest_component)

largest_subgraph_nodes = largest_subgraph.number_of_nodes()
largest_subgraph_edges = largest_subgraph.number_of_edges()
largest_subgraph_average_degree = (2 * largest_subgraph_edges) / largest_subgraph_nodes if largest_subgraph_nodes > 0 else 0
print("Largest Subgraph Number of Nodes:", largest_subgraph_nodes)
print("Largest Subgraph Number of Edges:", largest_subgraph_edges)
print("Largest Subgraph Average Degree:", largest_subgraph_average_degree)

# Step 2: Calculate Average Path Length
average_path_length = nx.average_shortest_path_length(largest_subgraph)

# Step 3: Calculate Clustering Coefficient
clustering_coefficient = nx.average_clustering(largest_subgraph)

print("Average Path Length:", average_path_length)
print("Clustering Coefficient:", clustering_coefficient)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
