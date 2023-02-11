types = [
    {"id": "car", "wheels": 4, "movement": "road"},
    {"id": "train", "wheels": 100, "movement": "railroad"},
    {"id": "motorbike", "wheels": 2, "movement": "road"},
    {"id": "airplane", "wheels": 10, "movement": "sky"},
]

transports = [
    {"maker": "Mercedes", "type": "car"},
    {"maker": "Italo", "type": "train"},
    {"maker": "Yamaha", "type": "motorbike"},
    {"maker": "BMW", "type": "car"},
    {"maker": "Audi", "type": "car"},
    {"maker": "Boeing", "type": "airplane"},
]


def list_of_wheels(option):
    result = []

    if option == "1":
        for transport in transports:
            value, *rest = [
                type["wheels"] for type in types if type["id"] == transport["type"]
            ]
            result.append(value)

        return result

    if option == "2":
        return [
            type["wheels"]
            for transport in transports
            for type in types
            if type["id"] == transport["type"]
        ]


option = input('Enter option "1" or "2"]: ')

result = list_of_wheels(option)

print(result)
