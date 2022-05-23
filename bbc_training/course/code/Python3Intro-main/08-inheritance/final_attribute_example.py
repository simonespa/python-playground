from typing import Final

class Window:
    BORDER_WIDTH: Final = 2.5

class ListView(Window):
    BORDER_WIDTH = 3  # Error: can't override a final attribute

window = Window()
print(window.BORDER_WIDTH)

window.BORDER_WIDTH = 3
print(window.BORDER_WIDTH)

listView = ListView()
print(listView.BORDER_WIDTH)
