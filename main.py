import TileGame

if __name__ == "__main__":
    level_one_builder = TileGame.TileGameLevelOneBuilder()
    director = TileGame.Director()
    director.construct(level_one_builder)
