import random

def create_graph():

    graph = {

        "Heart": {"Aorta":2, "Coronary":1},

        "Aorta": {"Carotid":2, "Systemic":3},

        "Carotid": {"Brain":1},

        "Coronary": {"HeartWall":1},

        "Systemic": {"Liver":2, "Kidney":2, "Abdomen":3},

        "Liver": {"HepaticVein":1},

        "Kidney": {"RenalVein":1},

        "Abdomen": {"Intestine":2},

        "Brain": {},
        "HeartWall": {},
        "HepaticVein": {},
        "RenalVein": {},
        "Intestine": {}
    }

    return graph


def heuristic():

    return {

        "Heart":4,
        "Aorta":3,
        "Carotid":1,
        "Brain":0,

        "Coronary":1,
        "HeartWall":0,

        "Systemic":2,

        "Liver":1,
        "Kidney":1,

        "Abdomen":2,
        "Intestine":0,

        "HepaticVein":0,
        "RenalVein":0
    }


def random_goal(graph, start="Heart"):

    nodes=list(graph.keys())

    if start in nodes:
        nodes.remove(start)

    return random.choice(nodes)