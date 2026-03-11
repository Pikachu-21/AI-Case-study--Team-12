import random


def dfs(graph, start, goal):

    stack = [[start]]
    visited = set()

    while stack:

        path = stack.pop()
        node = path[-1]

        if node == goal:
            print("DFS Path:", path)
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in graph[node]:
                stack.append(path + [neighbor])

    return None


def greedy_best_first(graph, start, goal, heuristic):

    open_list = [(heuristic[start], start, [start])]

    while open_list:

        open_list.sort()
        h, node, path = open_list.pop(0)

        if node == goal:
            print("Greedy Best First Path:", path)
            return path

        for neighbor in graph[node]:

            open_list.append((heuristic[neighbor], neighbor, path + [neighbor]))

    return None


def genetic_algorithm(graph, start, goal):

    nodes = list(graph.keys())

    population = [random.sample(nodes, 4) for _ in range(5)]

    best = population[0]

    print("Genetic Algorithm candidate:", best)

    return best