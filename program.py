from views.terminal import Terminal
from views.gui import ContactManagerGUI
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == "gui":
            ContactManagerGUI()
        elif sys.argv[1] == "terminal":
            Terminal()
        else:
            print("Not supported.")
    elif len(sys.argv) > 2:
        print("Not supported.")
    else:
        Terminal()