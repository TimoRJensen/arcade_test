import random
import arcade

WIDTH = 640
HEIGHT = 480
TITLE = "Example"

BLUE_GEM = ":resources:images/items/gemBlue.png"
GREEN_GEM = ":resources:images/items/gemGreen.png"
RED_GEM = ":resources:images/items/gemRed.png"

GEM_SCALE = 0.5


class Gem(arcade.Sprite):
    def __init__(
        self, sprite_string: str, center_x: float, center_y: float, speed: float = 0
    ):
        super().__init__(sprite_string, GEM_SCALE)
        self.center_x = center_x
        self.center_y = center_y
        self.speed = speed

    def random_move(self):
        speed = self.speed // 15
        self.center_x += random.randint(-speed, speed)
        self.center_y += random.randint(-speed, speed)

        if self.center_x < 0:
            self.center_x = 0
        elif self.center_x > WIDTH:
            self.center_x = WIDTH
        if self.center_y < 0:
            self.center_y = 0
        elif self.center_y > HEIGHT:
            self.center_y = HEIGHT
        arcade.check_for_collision()


class MyWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.gems = None
        self.draw_counter = 0

    def setup(self):
        self.gems: arcade.SpriteList[Gem] = arcade.SpriteList()

        blue_gem = Gem(BLUE_GEM, center_x=100, center_y=100, speed=100)
        green_gem = Gem(GREEN_GEM, center_x=200, center_y=100, speed=50)
        red_gem = Gem(RED_GEM, center_x=300, center_y=100, speed=25)

        self.gems.extend([blue_gem, green_gem, red_gem])

    def on_draw(self):
        self.draw_counter += 1
        self.clear(arcade.color.AERO_BLUE)
        for gem in self.gems:
            gem: Gem
            gem.random_move()

        self.gems.draw()


if __name__ == "__main__":
    window = MyWindow(WIDTH, HEIGHT, TITLE)
    window.setup()
    window.run()
