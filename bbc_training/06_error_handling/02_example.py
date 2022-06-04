# inventory = {
#   'milk': 2,
#   'bread': 5,
#   'wine': 3
# }

from inspect import trace
import traceback


class ProductSelectionError(Exception):
    pass


inventory = [("milk", 2), ("bread", 5), ("wine", 3)]


def get_another_price(index):
    try:
        i = int(index)
        return inventory[i][1]
    except IndexError as e:
        raise ProductSelectionError("lalla") from e


def get_price(index):
    i = int(index)

    if i > len(inventory):
        raise ProductSelectionError("Not a valid product")

    return inventory[i][1]


def store():
    print(inventory)
    try:
        prod = int(input("Pick a number: "))
        price = get_another_price(prod)
        print(f"{prod} costs {price}£")
    except ProductSelectionError as e:
        print(e)
    except IndexError:
        print(f"{prod} is not a valid index")
    except ValueError:
        print("Not a number")
    except:
        print("Something else went wrong")


store()
