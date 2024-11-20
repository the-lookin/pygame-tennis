import pygame

class Player:
    def __init__(self, screen, position, name, bat):
        self.screen = screen
        self.position = position
        self.name = name
        self.bat = bat
        self.score = 0
    
    def set_score(self):
        self.score += 1

    def draw_stat(self):
        font = pygame.font.SysFont('Arial', 24)
        text_surface = font.render(f'{self.name}: {self.score}', True, (255,255,255))

        y_pos_name = 10
        if self.position == 'left':
            x_pos_name = 40
        elif self.position == 'right':
            x_pos_name = self.screen.get_width() - text_surface.get_width() - 40
        
        self.screen.blit(text_surface, (x_pos_name, y_pos_name))