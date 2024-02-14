import sys

from sprites import *


class TileGame:
    def __init__(self):
        pg.init()
        # La Mise en place du jeu (carte, personnages, objets ...)
        self.game_set_up = None
        # L'interface graphique pour l'utilisateur
        self.graphical_user_interface = None
        # Les étapes du jeu (déroulement d'une partie)
        self.game_mechanics = None


# L'interface qui définit les méthodes nécessaire à la création de chaque composant du jeu.
class TileGameBuilder:
    def build_game_set_up(self):
        pass

    def build_graphical_user_interface(self):
        pass

    def build_game_mechanics(self):
        pass


class TileGameLevelOneBuilder(TileGameBuilder):
    def __init__(self):
        self.gf = GameFolder()
        self.level_one = "level one"

        self.game_set_up = GameSetUp(self.gf)
        self.graph_interface = GraphicalUserInterface(self.gf)
        self.game_mechanics = GameMechanics()

    def build_game_set_up(self):
        # Construction de la carte
        self.game_set_up.build_map(self.level_one, self.gf)

    def build_graphical_user_interface(self):
        self.graph_interface.show_go_screen(self.game_mechanics)

    def build_game_mechanics(self):
        self.game_mechanics.run(self.graph_interface, self.game_set_up, self.gf)


class Director:
    def construct(self, builder):
        builder.build_game_set_up()
        builder.build_game_mechanics()
        builder.build_graphical_user_interface()
        return builder


class GameSetUp:
    def __init__(self, game_folder):
        # La carte sur laquelle le jeu se déroule
        self.map = []
        # Les murs et cases impénétrables
        self.walls = pg.sprite.Group()
        # Éléments graphiques sur la carte
        # Personnages
        self.player = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        # Objets
        self.chest = pg.sprite.Group()
        self.red_key = pg.sprite.Group()
        self.blue_key = pg.sprite.Group()
        self.green_key = pg.sprite.Group()
        # Tous les éléments graphiques
        self.all_sprites = (pg.sprite.LayeredUpdates())
        # Le sac du joueur
        self.bag = []

    def build_map(self, map_data_level, game_folder):
        self.load_map_data(map_data_level, game_folder)
        game_folder.add_background_to_img_folder("img/map4.png")
        # nb = 0
        for row, tiles in enumerate(self.map):
            for col, tile in enumerate(tiles):
                if tile == "D":
                    self.walls.add(Wall(self, col, row))
                elif tile == "P":
                    self.player = Player(self, col, row)
                elif tile == "R":
                    self.red_key.add(Key(self, col, row,"red"))
                elif tile == "B":
                    self.blue_key.add(Key(self, col, row, "blue"))
                elif tile == "G":
                    self.green_key.add(Key(self, col, row, "green"))
                elif tile == "E":
                    self.enemies.add(Enemy(self, col, row))
                elif tile == "C":
                    self.chest.add(Chest(self, col, row))

                else:
                    pass  # Renvoyer une erreur

    def load_map_data(self, map_data_level, game_folder):
        with open(
                path.join(game_folder.game_folder, "maps/map.txt"), "rt"
        ) as f:  # self.select_map_path(map_data_level) instead of "maps/map.txt" ?
            for line in f:
                self.map.append(line)

    # method to get the right map -- work in progress
    def select_map_path(self, map_data_level):
        if map_data_level == "level one":
            return "maps/map.txt"
        elif map_data_level == "level two":
            pass  # projet futur
        else:
            pass


class GraphicalUserInterface:
    def __init__(self, game_folder):
        self.title_font = path.join(game_folder.font_folder, "Bouncy.otf")
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        pg.font.init()

    def show_go_screen(self, game_mechanics):
        self.screen.fill(BLACK)
        if game_mechanics.playing == 1:
            self.draw_text(
                "GAME OVER",
                self.title_font,
                100,
                GREEN,
                WIDTH / 2,
                HEIGHT / 2,
                align="center",
            )
            self.draw_text(
                "Press a key to start",
                self.title_font,
                50,
                WHITE,
                WIDTH / 2,
                HEIGHT * 3 / 4,
                align="center",
            )
            pg.display.flip()
            self.wait_for_key(game_mechanics)
        elif game_mechanics.playing == 2:
            self.draw_text(
                "VICTORY !",
                self.title_font,
                100,
                YELLOW,
                WIDTH / 2,
                HEIGHT / 2,
                align="center",
            )
            self.draw_text(
                "Press a key to start",
                self.title_font,
                50,
                WHITE,
                WIDTH / 2,
                HEIGHT * 3 / 4,
                align="center",
            )
            pg.display.flip()
            self.wait_for_key(game_mechanics)
        else:
            pass

    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self, game_mechanics):
        pg.event.wait()
        waiting = True
        while waiting:
            # self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    game_mechanics.quit()
                if event.type == pg.KEYUP:
                    waiting = False
                    game_mechanics.reset()


class GameFolder:
    def __init__(self):
        # Variables de gestion de documents annexes au jeu (images, police d'écriture ...)
        self.game_folder = path.dirname(__file__)
        self.img_folder = path.join(self.game_folder, "img")
        self.font_folder = path.join(self.game_folder, "font")

        self.background_img = None

    def add_background_to_img_folder(self, img):
        self.background_img = pg.image.load(img)

    def add_to_img_folder(self, img):
        pg.image.load(path.join(self.img_folder, img)).convert_alpha()

    def add_to_font_folder(self, font):
        pg.image.load(path.join(self.font_folder, font)).convert_alpha()


class GameMechanics:
    def __init__(self):
        self.playing = 0

    def run(self, graph_interface, game_set_up, game_folder):
        # La boucle de jeu
        while self.playing == 0:
            # self.dt = self.clock.tick(FPS) / 1000
            self.events(game_set_up)
            self.update(game_set_up)
            self.draw(graph_interface, game_folder, game_set_up)

    def events(self, game_set_up):
        # Détection des actions déclenchées par le joueur.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN:
                # new method here ?
                if event.key == pg.K_ESCAPE:
                    quit()
                elif event.key == pg.K_LEFT:
                    game_set_up.player.move(dx=-1)
                elif event.key == pg.K_RIGHT:
                    game_set_up.player.move(dx=1)
                elif event.key == pg.K_UP:
                    game_set_up.player.move(dy=-1)
                elif event.key == pg.K_DOWN:
                    game_set_up.player.move(dy=1)
                else:
                    pass  # détection d'erreurs
            else:
                pass  # détection d'erreurs

    def update(self, game_set_up):
        # Mise à jour des éléments graphiques en jeu
        game_set_up.all_sprites.update()

        # Le joueur ramasse la clé rouge.
        hit_red_key = pg.sprite.spritecollide(
            game_set_up.player, game_set_up.red_key, True
        )
        for i in hit_red_key:
            i.kill()
            game_set_up.bag.append("red key")

        # Le joueur ramasse la clé bleu.
        hit_blue_key = pg.sprite.spritecollide(
            game_set_up.player, game_set_up.blue_key, True
        )
        for j in hit_blue_key:
            j.kill()
            game_set_up.bag.append("blue key")

        # Le joueur ramasse la clé verte.
        hit_green_key = pg.sprite.spritecollide(
            game_set_up.player, game_set_up.green_key, True
        )
        for k in hit_green_key:
            k.kill()
            game_set_up.bag.append("green key")

        # Le joueur rencontre un ennemi.
        hit_enemy = pg.sprite.spritecollide(
            game_set_up.player, game_set_up.enemies, True  # game_set_up.__init__
        )
        if hit_enemy:
            self.playing = 1

        # Le joueur atteint le coffre. Trois clés sont nécessaire pour l'ouvrir et terminer le niveau.
        hit_chest = pg.sprite.spritecollide(
            game_set_up.player, game_set_up.chest, False
        )
        if hit_chest:
            if len(game_set_up.bag) == 3:
                self.playing = 2

    def draw(self, graph_interface, game_folder, game_set_up):
        graph_interface.screen.blit(
            game_folder.background_img, game_folder.background_img.get_rect()
        )
        game_set_up.all_sprites.draw(graph_interface.screen)
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()

    def reset(self):
        level_one_builder = TileGameLevelOneBuilder()
        director = Director()
        director.construct(level_one_builder)
