import sys
from src.cli.run import run_cli
from src.gui.run import run_gui

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        run_gui()
    else:
        run_cli()

if __name__ == "__main__":
    main()
