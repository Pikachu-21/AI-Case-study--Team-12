import heapq
import random


def uniform_cost_search(graph,start,goal):

    pq=[(0,start,[start])]
    visited=set()

    while pq:

        cost,node,path=heapq.heappop(pq)

        if node==goal:
            print("UCS Path:", " -> ".join(path))
            print("Cost:",cost)
            return path

        if node not in visited:

            visited.add(node)

            for neighbor,weight in graph[node].items():

                heapq.heappush(
                    pq,
                    (cost+weight,neighbor,path+[neighbor])
                )

    return None


def a_star_search(graph,start,goal,heuristic):

    pq=[(heuristic[start],0,start,[start])]
    visited=set()

    while pq:

        f,cost,node,path=heapq.heappop(pq)

        if node==goal:

            print("A* Path:", " -> ".join(path))
            print("Cost:",cost)

            return path

        if node not in visited:

            visited.add(node)

            for neighbor,weight in graph[node].items():

                g=cost+weight
                h=heuristic[neighbor]
                f=g+h

                heapq.heappush(
                    pq,
                    (f,g,neighbor,path+[neighbor])
                )

    return None


def adversarial_search(graph,start,goal):

    current=start
    path=[current]

    while current!=goal:

        neighbors=list(graph[current].keys())

        if not neighbors:
            return None

        current=random.choice(neighbors)
        path.append(current)

    print("Adversarial Path:", " -> ".join(path))

    return path