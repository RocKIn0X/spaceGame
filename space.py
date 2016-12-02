import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class SpaceGameWindow(arcade.Window):
    def _init_(self, width, height):
        super()._init_(width, height)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

if _name_ == '_main_':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()
