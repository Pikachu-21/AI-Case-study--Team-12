import heapq
import math


def uniform_cost_search(graph, start, goal):

    pq = [(0, start, [start])]
    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node == goal:
            print("UCS Path:", path)
            return path

        if node not in visited:

            visited.add(node)

            for neighbor, weight in graph[node].items():
                heapq.heappush(pq, (cost+weight, neighbor, path+[neighbor]))

    return None


def a_star(graph, start, goal, heuristic):

    pq = [(heuristic[start], 0, start, [start])]

    while pq:

        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            print("A* Path:", path)
            return path

        for neighbor, weight in graph[node].items():

            new_g = g + weight
            new_f = new_g + heuristic[neighbor]

            heapq.heappush(pq, (new_f, new_g, neighbor, path+[neighbor]))

    return None


def adversarial_search(graph, start, goal, heuristic):

    def minimax(node, depth, maximizing):

        if node == goal or depth == 0:
            return heuristic[node], [node]

        if maximizing:

            best = -math.inf
            best_path = []

            for neighbor in graph[node]:

                val, path = minimax(neighbor, depth-1, False)

                if val > best:
                    best = val
                    best_path = [node] + path

            return best, best_path

        else:

            best = math.inf
            best_path = []

            for neighbor in graph[node]:

                val, path = minimax(neighbor, depth-1, True)

                if val < best:
                    best = val
                    best_path = [node] + path

            return best, best_path


    score, path = minimax(start, 3, True)

    print("Adversarial Path:", path)

    return path