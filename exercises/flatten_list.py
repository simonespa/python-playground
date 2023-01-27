def flatten(list):
    result = []

    for sublist in list:
        result.extend(sublist)

    return result


def flatten_comprehension(list):
    return [el for sublist in list for el in sublist]
