def depth_limited_search(graph, start, goal, limit):

    stack = [(start, [start], 0)]

    while stack:

        node, path, depth = stack.pop()

        if node == goal:
            print("Depth Limited Path:", path)
            return path

        if depth < limit:

            for neighbor in graph[node]:
                stack.append((neighbor, path+[neighbor], depth+1))

    return None


def hill_climbing(graph, start, goal, heuristic):

    current = start
    path = [current]

    while current != goal:

        neighbors = graph[current]

        if not neighbors:
            break

        next_node = min(neighbors, key=lambda x: heuristic[x])

        if heuristic[next_node] >= heuristic[current]:
            print("Local optimum reached")
            return path

        current = next_node
        path.append(current)

    print("Hill Climbing Path:", path)

    return path


def first_order_logic(graph, start, goal):

    print("Applying logical inference")

    if goal in graph[start]:
        return [start, goal]

    return [start]