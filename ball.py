import pygame
import random
import math

class Ball:
    radius = 5
    color = (255, 255, 255)

    def __init__(self, screen, bats):
        self.screen = screen
        self.bats = bats
        self.reset()

    def reset(self):
        self.x = self.screen.get_width() / 2 + self.radius / 2
        self.y = self.screen.get_height() / 2 + self.radius / 2
        self.angle = self.start_angle()

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self, speed):
        # get radians
        radians = self.angle * (math.pi / 180)

        # get delta x and y
        dx = speed * math.cos(radians)
        dy = speed * math.sin(radians)

        # set curren x and y
        self.x = self.x + dx
        self.y = self.y + dy

        # fix collides
        if self.x >= self.screen.get_width() - self.radius \
            or self.x <= self.radius \
            or self.y >= self.screen.get_height() - self.radius \
            or self.y <= self.radius:
            self.collide()
        
        self.check_beat()
    
    def collide(self):
        # bounce of the wall
        if self.y >= self.screen.get_height() - self.radius or self.y <= self.radius:
            self.angle = -self.angle
    
    def check_miss(self):
        if self.x >= self.screen.get_width() - self.radius:
            return 'right'
        if self.x <= self.radius:
            return 'left'
        return False
    
    def check_beat(self):
        # bounce of the bats
        for bat in self.bats:
            if bat.player_index == 0: #left bat
                if self.x <= bat.x + self.radius + bat.width / 2 and (self.y >= bat.y and  self.y <= bat.y + bat.height):
                    self.x = bat.x + self.radius + bat.width / 2
                    offset = bat.y - self.y              
                    self.angle += 180 - offset / 2
            if bat.player_index == 1: #right bat
                if self.x >= bat.x - self.radius - bat.width / 2 and  (self.y >= bat.y and  self.y <= bat.y + bat.height):
                    self.x = bat.x - self.radius - bat.width / 2
                    offset = bat.y - self.y
                    self.angle += 180 - offset / 2


    def start_angle(self):
        # Get random angle in diapason (1,60) (120, 240), (300, 359)
        valid_angles = [x for x in range(361) if (1 < x < 60) or (120 < x < 240) or (300 < x < 359)]
        return random.choice(valid_angles)