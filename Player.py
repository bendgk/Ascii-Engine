import GameMap

screen = GameMap.game_map()

class player:
    def __init__(self, sprite, user):
        self.user = user
        self.player_sprite = sprite
        self.x = len(screen.Map[0])/2 - 1
        self.y = len(screen.Map)/2 - 1
        self.prev_x = len(screen.Map[0])/2 - 1
        self.prev_y = len(screen.Map)/2 - 1
    def Transform(self, key):
        if key == "w":
            self.prev_x = self.x
            self.prev_y = self.y
            self.y += -1
        elif key == "s":
            self.prev_x = self.x
            self.prev_y = self.y
            self.y += 1
        elif key == "d":
            self.prev_x = self.x
            self.prev_y = self.y
            self.x += 1
        elif key == "a":
            self.prev_x = self.x
            self.prev_y = self.y
            self.x += -1
