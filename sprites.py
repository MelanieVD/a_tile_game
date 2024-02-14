from os import path

import pygame as pg

from settings import *


# Is it a good idea to do heritage among sprite classes ?
class Characters(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game


# Cette classe caractérise le personnage que le joueur pourra manipuler
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self._layer = PLAYER_LAYER
        self.image = pg.image.load(
            path.join("img", PLAYER_IMG)
        ).convert_alpha()  # game.player_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False


# Cette classe caractérise les ennemis que le joueur pourra rencontrer dans le jeu.
class Enemy(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        self._layer = ENEMY_LAYER
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(
            path.join("img", ENEMY_IMG)
        ).convert_alpha()  # game.ennemi_img
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    # def update(self):
    #     self.rect.x = self.x * TILESIZE
    #     self.rect.y = self.y * TILESIZE


# Cette classe permet la création des murs et tuiles impénétrables dans le jeu.
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = WALL_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


# Cette classe permet de créer les clés nécessaire à l'ouverture du coffre.
class Key(pg.sprite.Sprite):
    def __init__(self, game, x, y, colour):
        self._layer = KEY_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.colour = colour
        if self.colour == "red":
            self.image = pg.image.load(
                path.join("img", RED_KEY_IMG)
            ).convert_alpha()
        elif self.colour == "blue":
            self.image = pg.image.load(
                path.join("img", BLUE_KEY_IMG)
            ).convert_alpha()
        elif self.colour == "green":
            self.image = pg.image.load(
                path.join("img", GREEN_KEY_IMG)
            ).convert_alpha()
        else:
            pass  # détection d'erreurs
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

    def kill(self):
        pg.sprite.Sprite.kill(self)


class Chest(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        # self._layer = CHEST_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(
            path.join("img", CHEST_IMG)
        ).convert_alpha()  # game.chest_img
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
