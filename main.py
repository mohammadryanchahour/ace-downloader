import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)

from src.interfaces.cli import CLI
from src.interfaces.gui import GUI
from PyQt5.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)  # Create the QApplication instance

    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        gui = GUI()  # Create GUI instance
        gui.show()
        sys.exit(app.exec_())  # Start the application event loop
    else:
        CLI()

if __name__ == "__main__":
    main()
