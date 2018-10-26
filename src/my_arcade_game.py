"""
Sprite Bullets

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_bullets
"""
import random
import arcade
import os

# Gameshell Keymappings
GAMESHELL_A = arcade.key.J
GAMESHELL_Y = arcade.key.I
GAMESHELL_X = arcade.key.U
GAMESHELL_B = arcade.key.K
GAMESHELL_START = arcade.key.ENTER
GAMESHELL_MENU = arcade.key.ESCAPE
GAMESHELL_SELECT = arcade.key.SPACE
GAMESHELL_SHIFT_A = arcade.key.H
GAMESHELL_SHIFT_Y = arcade.key.O
GAMESHELL_SHIFT_X = arcade.key.Y
GAMESHELL_SHIFT_B = arcade.key.L
GAMESHELL_SHIFT_SELECT = arcade.key.MINUS
GAMESHELL_SHIFT_START = arcade.key.PLUS
GAMESHELL_SHIFT_MENU = arcade.key.BACKSPACE


SPRITE_SCALING_PLAYER = 0.3
SPRITE_SCALING_COIN = 0.15
SPRITE_SCALING_LASER = 0.4
COIN_COUNT = 5

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240

BULLET_SPEED = 7
MOVEMENT_SPEED = 3

READY = 0
RUNNING = 1
YOU_WON = 2
YOU_LOST = 3

class PlayerSprite(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "")

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        self.state = READY

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = PlayerSprite("images/character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 20
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("images/coin_01.png", SPRITE_SCALING_COIN)

            # Position the coin
            while coin.left < 0 or coin.right > SCREEN_WIDTH:
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)
                coin.change_x = random.randrange(-1, 2)
                coin.change_y = random.randrange(-1, 2)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 5, SCREEN_HEIGHT - 12, arcade.color.WHITE, 12)

        line_height = 20
        font_size = 16
        text_color = arcade.color.BLACK
        if self.state == YOU_WON:
            y_pos = SCREEN_HEIGHT / 2 + 16
            arcade.draw_text(f"You Won!", 10, y_pos, text_color, font_size)
            y_pos -= line_height
            arcade.draw_text(f"Press Select To Restart", 10, y_pos, text_color, font_size)
            y_pos -= line_height
            arcade.draw_text(f"Press Menu To Exit", 10, y_pos, text_color, font_size)

        if self.state == READY:
            y_pos = SCREEN_HEIGHT / 2 + 16
            arcade.draw_text(f"Arrow keys move, buttons fire", 10, y_pos, text_color, font_size)
            y_pos -= line_height
            arcade.draw_text(f"Press start to begin", 10, y_pos, text_color, font_size)
            y_pos -= line_height
            arcade.draw_text(f"Press menu to exit", 10, y_pos, text_color, font_size)


    def player_shoot(self, angle, change_x, change_y):
        bullet = arcade.Sprite("images/laserBlue01.png", SPRITE_SCALING_LASER)
        bullet.change_y = change_y
        bullet.change_x = change_x
        bullet.angle = angle
        bullet.center_x = self.player_sprite.center_x
        bullet.center_y = self.player_sprite.center_y
        self.bullet_list.append(bullet)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # Gameshell Arrow Keypad
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

        # Gameshell "A" key
        elif key == GAMESHELL_A:
            self.player_shoot(angle=270, change_x=0, change_y=-BULLET_SPEED)

        # Gameshell "Y" key
        elif key == GAMESHELL_Y:
            self.player_shoot(angle=90, change_x=0, change_y=BULLET_SPEED)

        # Gameshell "X" key
        elif key == GAMESHELL_X:
            self.player_shoot(angle=180, change_x=-BULLET_SPEED, change_y=0)

        # Gameshell "B" key
        elif key == GAMESHELL_B:
            self.player_shoot(angle=0, change_x=BULLET_SPEED, change_y=0)

        # Gameshell "Start" button
        elif key == GAMESHELL_SELECT and (self.state == YOU_LOST or self.state == YOU_WON):
            self.setup()
            self.state = READY

        elif key == GAMESHELL_START and self.state == READY:
            self.state = RUNNING

        # Gameshell "Menu" button
        elif key == GAMESHELL_MENU:
            exit()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        if self.state == RUNNING:
            self.coin_list.update()
            self.bullet_list.update()
            self.player_list.update()

            for coin in self.coin_list:
                if coin.left < 0 and coin.change_x < 0:
                    coin.change_x *= -1
                if coin.right > SCREEN_WIDTH and coin.change_x > 0:
                    coin.change_x *= -1
                if coin.top > SCREEN_HEIGHT and coin.change_y > 0:
                    coin.change_y *= -1
                if coin.bottom < 0 and coin.change_y < 0:
                    coin.change_y *= -1

            # Loop through each bullet
            for bullet in self.bullet_list:

                # Check this bullet to see if it hit a coin
                hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

                # If it did, get rid of the bullet
                if len(hit_list) > 0:
                    bullet.kill()

                # For every coin we hit, add to the score and remove the coin
                for coin in hit_list:
                    coin.kill()
                    self.score += 1

                    # Hit Sound
                    # arcade.sound.play_sound(self.hit_sound)

                # If the bullet flies off-screen, remove it.
                if bullet.bottom > SCREEN_HEIGHT or bullet.top < 0 or bullet.left > SCREEN_WIDTH or bullet.right < 0:
                    bullet.kill()

            if len(self.coin_list) == 0:
                self.state = YOU_WON


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
