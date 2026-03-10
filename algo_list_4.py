import random


def iterative_deepening(graph,start,goal):

    stack=[(start,[start])]
    visited=set()

    while stack:

        node,path=stack.pop()

        if node==goal:
            print("IDS Path:", " -> ".join(path))
            return path

        visited.add(node)

        for neighbor in graph[node]:
            stack.append((neighbor,path+[neighbor]))

    return None


def recursive_best_first_search(graph,start,goal,heuristic):

    current=start
    path=[current]

    while current!=goal:

        neighbors=list(graph[current].keys())

        if not neighbors:
            return None

        next_node=min(neighbors,key=lambda x:heuristic[x])

        current=next_node
        path.append(current)

    print("RBFS Path:", " -> ".join(path))

    return path


def constraint_satisfaction(graph,start,goal):

    current=start
    path=[current]

    while current!=goal:

        neighbors=list(graph[current].keys())

        if not neighbors:
            return None

        current=random.choice(neighbors)
        path.append(current)

    print("CSP Path:", " -> ".join(path))

    return path