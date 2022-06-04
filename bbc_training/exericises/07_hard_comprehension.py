species = [
    {"name": "Human", "legs": 2, "movement": "walk"},
    {"name": "Dog", "legs": 4, "movement": "walk"},
    {"name": "Duck", "legs": 2, "movement": "fly"},
    {"name": "Whale", "legs": 0, "movement": "swim"},
]

individuals = [
    {"name": "Bob", "species": "Human"},
    {"name": "Daffy", "species": "Duck"},
    {"name": "Lassie", "species": "Dog"},
    {"name": "Moby", "species": "Whale"},
    {"name": "Lisa", "species": "Human"},
    {"name": "Pluto", "species": "Dog"},
]


def comprehension(option):
    if option == "1":
        theSum = 0
        for individual in individuals:
            theSum += sum(
                [
                    specie["legs"]
                    for specie in species
                    if specie["name"] == individual["species"]
                ]
            )

        return theSum

    if option == "2":
        return sum(
            [
                spec["legs"]
                for individual in individuals
                for spec in species
                if spec["name"] == individual["species"]
            ]
        )


option = input('Enter option "1" or "2"]: ')

result = comprehension(option)
print(result)
