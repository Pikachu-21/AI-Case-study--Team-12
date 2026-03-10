from graph import create_graph, heuristic, random_goal
import graph_visualisation as graph_visualization

import algo_list_1 as s1
import algo_list_2 as s2
import algo_list_3 as s3
import algo_list_4 as s4
import algo_list_5 as s5


graph=create_graph()
h=heuristic()

start="Heart"


def menu():

    print("\n===== NANOROBOT AI CONTROL SYSTEM =====\n")

    print("Algorithm List 1: Kalla Aravindh")
    print("1 BFS")
    print("2 Bidirectional Search")
    print("3 Simulated Annealing\n")

    print("Algorithm List 2: Mohammad Amman")
    print("4 DFS")
    print("5 Greedy Best First")
    print("6 Genetic Algorithm\n")

    print("Algorithm List 3: Madduru Vaishnavi")
    print("7 Uniform Cost Search")
    print("8 A* Search")
    print("9 Adversarial Search\n")

    print("Algorithm List 4: Rentapalli Saahi")
    print("10 Iterative Deepening")
    print("11 Recursive Best First Search")
    print("12 Constraint Satisfaction\n")

    print("Algorithm List 5: Lonja Hemaanvi")
    print("13 Depth Limited Search")
    print("14 Hill Climbing")
    print("15 First Order Logic\n")

    print("0 Exit")


while True:

    menu()

    try:

        choice=int(input("Enter choice: "))

        if choice==0:
            break

        goal=random_goal(graph,start)

        print("\n⚠ Foreign cell detected at:",goal)

        path=None

        if choice==1:
            path=s1.bfs(graph,start,goal)

        elif choice==2:
            path=s1.bidirectional_search(graph,start,goal)

        elif choice==3:
            path=s1.simulated_annealing(graph,start,goal)

        elif choice==4:
            path=s2.dfs(graph,start,goal)

        elif choice==5:
            path=s2.greedy_best_first_search(graph,start,goal,h)

        elif choice==6:
            path=s2.genetic_algorithm(graph,start,goal)

        elif choice==7:
            path=s3.uniform_cost_search(graph,start,goal)

        elif choice==8:
            path=s3.a_star_search(graph,start,goal,h)

        elif choice==9:
            path=s3.adversarial_search(graph,start,goal)

        elif choice==10:
            path=s4.iterative_deepening(graph,start,goal)

        elif choice==11:
            path=s4.recursive_best_first_search(graph,start,goal,h)

        elif choice==12:
            path=s4.constraint_satisfaction(graph,start,goal)

        elif choice==13:
            path=s5.depth_limited_search(graph,start,goal)

        elif choice==14:
            path=s5.hill_climbing(graph,start,goal,h)

        elif choice==15:
            path=s5.first_order_logic(graph,start,goal)

        else:
            print("Invalid choice")
            continue

        if path:

            sim=input("\nSimulate traversal? (y/n): ")

            if sim.lower()=="y":
                graph_visualization.animate_traversal(graph,path)

        else:
            print("Nanobot could not reach target.")

    except:
        print("Invalid input")