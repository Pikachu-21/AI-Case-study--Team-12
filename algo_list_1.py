from collections import deque
import random


def bfs(graph,start,goal):

    queue=deque([(start,[start])])
    visited=set()

    while queue:

        node,path=queue.popleft()

        if node==goal:
            print("BFS Path:", " -> ".join(path))
            return path

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                queue.append((neighbor,path+[neighbor]))

    return None


def bidirectional_search(graph,start,goal):

    queue=deque([(start,[start])])
    visited=set()

    while queue:

        node,path=queue.popleft()

        if node==goal:
            print("Bidirectional Path:", " -> ".join(path))
            return path

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                queue.append((neighbor,path+[neighbor]))

    return None


def simulated_annealing(graph,start,goal):

    current=start
    path=[current]

    while current!=goal:

        neighbors=list(graph[current].keys())

        if not neighbors:
            return None

        current=random.choice(neighbors)
        path.append(current)

    print("Simulated Annealing Path:", " -> ".join(path))

    return path