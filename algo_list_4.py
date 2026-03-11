import math


def depth_limited_search(graph, node, goal, limit, path):

    if node == goal:
        return path

    if limit <= 0:
        return None

    for neighbor in graph[node]:

        result = depth_limited_search(graph, neighbor, goal, limit-1, path+[neighbor])

        if result:
            return result

    return None


def iterative_deepening_search(graph, start, goal):

    depth = 0

    while True:

        result = depth_limited_search(graph, start, goal, depth, [start])

        if result:
            print("IDS Path:", result)
            return result

        depth += 1


def recursive_best_first_search(graph, start, goal, heuristic):

    def rbfs(node, path, g, limit):

        if node == goal:
            return path, g

        successors = []

        for neighbor, cost in graph[node].items():

            new_g = g + cost
            f = new_g + heuristic[neighbor]

            successors.append((neighbor, f, new_g))

        if not successors:
            return None, math.inf

        while True:

            successors.sort(key=lambda x: x[1])

            best = successors[0]

            if best[1] > limit:
                return None, best[1]

            alt = successors[1][1] if len(successors) > 1 else math.inf

            result, best_f = rbfs(best[0], path+[best[0]], best[2], min(limit, alt))

            successors[0] = (best[0], best_f, best[2])

            if result:
                return result, best_f


    path, cost = rbfs(start, [start], 0, math.inf)

    print("RBFS Path:", path)

    return path


def constraint_satisfaction(graph, start, goal):

    print("Checking constraints")

    if goal in graph[start]:
        return [start, goal]

    return [start]