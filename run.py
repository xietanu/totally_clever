"""
The entry point for the application to be run from the command line.
"""
from arcade import run
from game import TotallyClever


def main():
    """Main function"""
    window = TotallyClever()
    window.setup()
    run()


if __name__ == "__main__":
    main()
