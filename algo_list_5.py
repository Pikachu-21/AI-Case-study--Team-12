import random


def depth_limited_search(graph,start,goal,limit=5):

    stack=[(start,[start],0)]

    while stack:

        node,path,depth=stack.pop()

        if node==goal:
            print("DLS Path:", " -> ".join(path))
            return path

        if depth<limit:

            for neighbor in graph[node]:
                stack.append((neighbor,path+[neighbor],depth+1))

    return None


def hill_climbing(graph,start,goal,heuristic):

    current=start
    path=[current]

    while current!=goal:

        neighbors=list(graph[current].keys())

        if not neighbors:
            return None

        next_node=min(neighbors,key=lambda x:heuristic[x])

        if heuristic[next_node] >= heuristic[current]:
            return None

        current=next_node
        path.append(current)

    print("Hill Climbing Path:", " -> ".join(path))

    return path


def first_order_logic(graph,start,goal):

    current=start
    path=[current]

    while current!=goal:

        neighbors=list(graph[current].keys())

        if not neighbors:
            return None

        current=random.choice(neighbors)
        path.append(current)

    print("FOL Path:", " -> ".join(path))

    return path