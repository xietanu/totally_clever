"""
The entry point for the application to be run from the command line.
"""
import arcade
import game

def main():
    """Main function"""
    game_instance = game.TotallyClever()
    game_instance.setup()
    arcade.run()


if __name__ == "__main__":
    main()
