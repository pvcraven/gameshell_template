import arcade

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, fullscreen=True)

        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, arcade.color.RED)
        arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, arcade.color.BLUE)

    def on_key_press(self, symbol: int, modifiers: int):
        exit()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
