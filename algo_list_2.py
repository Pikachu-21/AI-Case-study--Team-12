import random


def dfs(graph,start,goal):

    stack=[(start,[start])]
    visited=set()

    while stack:

        node,path=stack.pop()

        if node==goal:
            print("DFS Path:", " -> ".join(path))
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in graph[node]:
                stack.append((neighbor,path+[neighbor]))

    return None


def greedy_best_first_search(graph,start,goal,heuristic):

    current=start
    path=[current]

    while current!=goal:

        neighbors=list(graph[current].keys())

        if not neighbors:
            return None

        next_node=min(neighbors,key=lambda x:heuristic[x])

        current=next_node
        path.append(current)

    print("Greedy Path:", " -> ".join(path))

    return path


def genetic_algorithm(graph,start,goal):

    current=start
    path=[current]

    while current!=goal:

        neighbors=list(graph[current].keys())

        if not neighbors:
            return None

        current=random.choice(neighbors)
        path.append(current)

    print("Genetic Algorithm Path:", " -> ".join(path))

    return path