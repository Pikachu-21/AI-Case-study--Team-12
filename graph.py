graph = {

    "Heart": {
        "Aorta": 5,
        "Pulmonary": 8
    },

    "Aorta": {
        "Carotid": 25,
        "Renal": 30
    },

    "Pulmonary": {
        "Lungs": 12
    },

    "Carotid": {
        "Brain": 15
    },

    "Renal": {
        "Kidney": 10
    },

    "Lungs": {},
    "Brain": {},
    "Kidney": {}
}

heuristic = {

    "Heart": 10,
    "Aorta": 7,
    "Pulmonary": 9,
    "Carotid": 2,
    "Renal": 5,
    "Lungs": 8,
    "Brain": 0,
    "Kidney": 4
}