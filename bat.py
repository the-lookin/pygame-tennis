import pygame

class Bat:
    width = 10
    height = 100

    def __init__(self, screen, color, player_index):
        self.screen = screen
        self.color = color
        self.player_index = player_index
        self.x = self.width
        self.y = self.screen.get_height() / 2 - self.height / 2
        if player_index == 1:
            self.x = self.screen.get_width() - self.width * 2
        self.draw()

    def reset(self):
        self.y = self.screen.get_height() / 2 - self.height / 2

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def move(self, y, speed):
        self.y += y * speed
        
        if self.y >= self.screen.get_height() - speed - self.height:
            self.y = self.screen.get_height() - speed - self.height
        
        if self.y <= speed:
            self.y = speed

    def collide(self):
        pass