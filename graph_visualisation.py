import networkx as nx
import matplotlib.pyplot as plt


def get_body_layout():

    pos = {

        "Brain": (0,5),
        "Carotid": (0,4),
        "Aorta": (0,3),

        "Coronary": (-1,2),
        "Heart": (0,2),

        "Systemic": (0,1),

        "Liver": (-1,0),
        "Kidney": (1,0),

        "Abdomen": (0,-1),

        "Intestine": (0,-2),

        "HepaticVein": (-1,-1),
        "RenalVein": (1,-1),

        "HeartWall": (-1,1)
    }

    return pos


def animate_traversal(graph,path):

    G=nx.DiGraph()

    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node,neighbor)

    pos=get_body_layout()

    plt.figure(figsize=(6,8))

    for i in range(len(path)):

        plt.clf()

        colors=[]

        for node in G.nodes():

            if node==path[i]:
                colors.append("red")

            elif node in path[:i]:
                colors.append("green")

            else:
                colors.append("skyblue")

        nx.draw_networkx(
            G,
            pos,
            node_color=colors,
            node_size=2000,
            font_size=9
        )

        plt.title("Nanobot Traversal")

        plt.pause(1)

    plt.show()