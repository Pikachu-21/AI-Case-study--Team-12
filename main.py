import graph as graph_env
import graph_visualisation as visualize

import algo_list_1 as s1
import algo_list_2 as s2
import algo_list_3 as s3
import algo_list_4 as s4
import algo_list_5 as s5

graph = graph_env.graph
heuristic = graph_env.heuristic


# INPUT VALIDATION FUNCTION
def validate_nodes(graph, start, goal):

    start = start.strip().title()
    goal = goal.strip().title()

    if start not in graph:
        print(f"\nStart node '{start}' not found.")
        print("Available nodes:", list(graph.keys()))
        return None, None

    if goal not in graph:
        print(f"\nGoal node '{goal}' not found.")
        print("Available nodes:", list(graph.keys()))
        return None, None

    if start == goal:
        print("\nStart and Goal nodes cannot be the same.")
        return None, None

    return start, goal


while True:

    print("\nAlgorithm list, student wise:")
    print("Algorithm 1-3: 2023004515: Kalla Aravindh")
    print("1  BFS")
    print("2  Bidirectional Search")
    print("3  Simulated Annealing\n")
    print("Algorithm 4-6: 2023000835: Mohammad Amman")
    print("4  DFS")
    print("5  Greedy Best First Search")
    print("6  Genetic Algorithm\n")
    print("Algorithm 7-9: 2023001606:Madduru Vaishnavi")
    print("7  Uniform Cost Search")
    print("8  A* Search")
    print("9  Adversarial Search\n")
    print("Algorithm 10-12: 2023006145: Rentapalli Saahi")
    print("10 Iterative Deepening Search")
    print("11 Recursive Best First Search")
    print("12 Constraint Satisfaction Problem\n")
    print("Algorithm 13-15: 2023003339: Lonja Hemaanvi")
    print("13 Depth Limited Search")
    print("14 Hill Climbing")
    print("15 First Order Logic\n")
    print("16 Exit")

    choice = input("\nEnter choice: ")

    if choice == "16":
        print("Exiting program...")
        break

    print("\nAvailable Nodes:", ", ".join(graph.keys()))

    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    start, goal = validate_nodes(graph, start, goal)

    if start is None:
        continue

    path = None

    if choice == "1":
        path = s1.bfs(graph, start, goal)

    elif choice == "2":
        path = s1.bidirectional_search(graph, start, goal)

    elif choice == "3":
        path = s1.simulated_annealing(graph, start, goal)

    elif choice == "4":
        path = s2.dfs(graph, start, goal)

    elif choice == "5":
        path = s2.greedy_best_first(graph, start, goal, heuristic)

    elif choice == "6":
        path = s2.genetic_algorithm(graph, start, goal)

    elif choice == "7":
        path = s3.uniform_cost_search(graph, start, goal)

    elif choice == "8":
        path = s3.a_star(graph, start, goal, heuristic)

    elif choice == "9":
        path = s3.adversarial_search(graph, start, goal, heuristic)

    elif choice == "10":
        path = s4.iterative_deepening_search(graph, start, goal)

    elif choice == "11":
        path = s4.recursive_best_first_search(graph, start, goal, heuristic)

    elif choice == "12":
        path = s4.constraint_satisfaction(graph, start, goal)

    elif choice == "13":
        path = s5.depth_limited_search(graph, start, goal, 3)

    elif choice == "14":
        path = s5.hill_climbing(graph, start, goal, heuristic)

    elif choice == "15":
        path = s5.first_order_logic(graph, start, goal)

    else:
        print("\nInvalid choice. Please select a valid option.")
        continue

    if path:
        visualize.visualize_traversal(graph, path)

    else:
        print("\nNo traversal path returned by the algorithm.")