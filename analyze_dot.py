import networkx as nx

if __name__ == "__main__":
    G = nx.Graph(nx.nx_pydot.read_dot(path))