import pygame
from bat import Bat
from ball import Ball
from player import Player

# size of screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 640

BAT_SPEED = 10
BALL_SPEED = 15
BACKGROUND_COLOR = (0, 0, 0)

LIGHT_GRAY_COLOR = (210, 210, 210)
WHITE_COLOR = (255, 255, 255)

POINTS_TO_WIN = 10

process_game = True

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Init game elements
player0_bat = Bat(screen, (255, 0, 255), 0)
player1_bat = Bat(screen, (0, 255, 0), 1)

game_ball = Ball(screen, (player0_bat, player1_bat))

player0 = Player(screen, 'left', 'Foo', player0_bat)
player1 = Player(screen, 'right', 'Bar', player1_bat)

def get_winner(player0, player1):
    if player0.score > player1.score:
        return player0
    else:
        return player1

def end_game(player0, player1, screen):
    # pause all objects
    global process_game
    winner = get_winner(player0, player1)
    process_game = False

    # draw end screen
    pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(200, 100, screen.get_width() - 200 * 2, screen.get_height() - 100 * 2))

    font_pre_winner = pygame.font.SysFont('Arrial', 36)
    font_winner = pygame.font.SysFont('Arrial', 86)
    font_score = pygame.font.SysFont('Arrial', 120)

    pre_winner_surface = font_pre_winner.render('Win!', True, LIGHT_GRAY_COLOR)
    winner_surface = font_winner.render(winner.name, True, WHITE_COLOR)
    score_surface = font_score.render(f'{player0.score} : {player1.score}', True, WHITE_COLOR)

    pre_winner_pos_x = screen.get_width() / 2 - pre_winner_surface.get_width() / 2
    pre_winner_pos_y = 200
    winner_pos_x = screen.get_width() / 2 - winner_surface.get_width() / 2
    winner_pos_y = 240
    score_pos_x = screen.get_width() / 2 - score_surface.get_width() / 2
    score_pos_y = 320

    screen.blit(pre_winner_surface, (pre_winner_pos_x, pre_winner_pos_y))
    screen.blit(winner_surface, (winner_pos_x, winner_pos_y))
    screen.blit(score_surface, (score_pos_x, score_pos_y))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    if process_game:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            player0_bat.move(1, BAT_SPEED)
        if keys[pygame.K_w]:
            player0_bat.move(-1, BAT_SPEED)

        if keys[pygame.K_DOWN]:
            player1_bat.move(1, BAT_SPEED)
        if keys[pygame.K_UP]:
            player1_bat.move(-1, BAT_SPEED)
        
        player0_bat.draw()
        player1_bat.draw()

        game_ball.draw()
        game_ball.move(BALL_SPEED)

        miss = game_ball.check_miss()    
        if miss == 'left':
            player1.set_score()
        if miss == 'right':
            player0.set_score()

        player0.draw_stat()
        player1.draw_stat()

        if miss:
            player0_bat.reset()
            player1_bat.reset()
            game_ball.reset()


    if (player0.score >= POINTS_TO_WIN or player1.score >= POINTS_TO_WIN):
        end_game(player0, player1, screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
