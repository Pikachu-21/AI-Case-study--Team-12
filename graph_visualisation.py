import networkx as nx
import matplotlib.pyplot as plt


def visualize_traversal(graph, path):

    G = nx.DiGraph()

    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    for i in range(len(path)):

        plt.clf()

        colors = []

        for node in G.nodes():

            if node == path[i]:
                colors.append("red")

            elif node in path[:i]:
                colors.append("green")

            else:
                colors.append("lightblue")

        nx.draw(G, pos, with_labels=True, node_color=colors)

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.pause(1)

    plt.show()