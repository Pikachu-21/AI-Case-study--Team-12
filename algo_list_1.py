from collections import deque
import random


def bfs(graph, start, goal):

    queue = deque([[start]])
    visited = set()

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node == goal:
            print("BFS Path:", path)
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in graph[node]:
                queue.append(path + [neighbor])

    return None


def bidirectional_search(graph, start, goal):

    queue = deque([[start]])

    while queue:

        path = queue.popleft()
        node = path[-1]

        for neighbor in graph[node]:

            new_path = path + [neighbor]

            if neighbor == goal:
                print("Bidirectional Path:", new_path)
                return new_path

            queue.append(new_path)

    return None


def simulated_annealing(graph, start, goal):

    current = start
    path = [current]
    temperature = 100

    while temperature > 1:

        neighbors = list(graph[current].keys())

        if not neighbors:
            break

        next_node = random.choice(neighbors)

        path.append(next_node)
        current = next_node

        if current == goal:
            print("Goal reached using Simulated Annealing")
            return path

        temperature *= 0.9

    return path