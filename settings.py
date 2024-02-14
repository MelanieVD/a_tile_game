# vec = pg.math.Vector2


# colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
# LIGHTGREY = (100, 100, 100)
GREEN = (111, 169, 66)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 736  # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 736  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Find three keys to open the chest"

TILESIZE = 92
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_IMG = "caracter2.png"

# keys
# ITEM_IMAGES = {'red key': 'red_key.png', 'blue key': 'blue_key.png', 'green key': 'green_key.png'}
RED_KEY_IMG = "red_key.png"
BLUE_KEY_IMG = "blue_key.png"
GREEN_KEY_IMG = "green_key.png"
ENEMY_IMG = "Enemy.png"
CHEST_IMG = "Chest.png"

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
KEY_LAYER = 3
# BLUE_KEY_LAYER = 3
# GREEN_KEY_LAYER = 3
ENEMY_LAYER = 2
CHEST_LAYER = 3
