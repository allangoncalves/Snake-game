import random
import pygame
from constants import *


def quit_game():
    pygame.quit()
    quit()


def apple_create():
    return (
        round(random.randrange(0, DISPLAY_WIDTH - BLOCK_SIZE), -1),
        round(random.randrange(0, DISPLAY_HEIGHT - BLOCK_SIZE), -1)
    )

def pause():
    GAME_DISPLAY.fill(WHITE)
    GAME_DISPLAY.blit(PAUSE_IMAGE, [280, 35])
    message_to_screen("Paused", RED, 20, 'L')
    message_to_screen("Press r for Resume and q for Quit", RED, 90, 's')
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return
                elif event.key == pygame.K_q:
                    quit_game()


def score(score):
    text = FONT.render("SCORE:" + str(score), True, BLACK)
    GAME_DISPLAY.blit(text, [0, 0])


def shortcuts():
    GAME_DISPLAY.fill(WHITE)
    message_to_screen("Shortcuts for snake game", GREEN, -200, 'L')
    message_to_screen("Play -> p", BLACK, -100, 's')
    message_to_screen("Quit -> q", BLACK, -55, 's')
    message_to_screen("Pause -> b", BLACK, 80, 's')
    message_to_screen("Resume -> r", BLACK, 125, 's')
    message_to_screen("Back -> e", BLACK, -10, 's')
    message_to_screen("Shortcuts -> s", BLACK, 170, 's')
    message_to_screen("Home -> h", BLACK, 35, 's')
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e or event.key == pygame.K_h:
                    return
                if event.key == pygame.K_q:
                    quit_game()


def intro():
    while True:
        GAME_DISPLAY.fill(WHITE)
        GAME_DISPLAY.blit(BACKGROUND_IMAGE, [85, 50])
        message_to_screen("Welcome to snake game", GREEN, -200, 'L')
        message_to_screen("Press q for Quit", BLACK, -100, 's')
        message_to_screen("Press p for Play", BLACK, -50, 's')
        message_to_screen("Press s for Shortcuts", BLACK, 0, 's')
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                elif event.key == pygame.K_q:
                    quit_game()
                elif event.key == pygame.K_s:
                    shortcuts()


def text_objects(text, color, size):
    if size == "L":
        text_surface = LFONT.render(text, True, color)
    else:
        text_surface = FONT.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_to_screen(msg, color, y_displace, size):
    textsurf, textrect = text_objects(msg, color, size)
    textrect.center = (DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2) + y_displace
    GAME_DISPLAY.blit(textsurf, textrect)


def snake_create(snakelist):
    for XY in snakelist:
        pygame.draw.rect(GAME_DISPLAY, GREEN, [XY[0], XY[1], BLOCK_SIZE, BLOCK_SIZE])


def game_over():
    message_to_screen("Game over", RED, -200, 'L')
    message_to_screen("Press p for Play again!", BLACK, -100, 's')
    message_to_screen("Press q for Quit!", BLACK, -50, 's')
    message_to_screen("Press h for Home!", BLACK, 0, 's')
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit_game()
                if event.key == pygame.K_h:
                    intro()
                if event.key == pygame.K_p:
                    gameloop()


def gameloop():
    randappleX, randappleY = apple_create()
    lead_x = DISPLAY_WIDTH / 2
    lead_y = DISPLAY_HEIGHT / 2
    snakelist = []
    snakelength = 1
    lead_x_change = 0
    lead_y_change = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = BLOCK_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = BLOCK_SIZE
                    lead_x_change = 0
                elif event.key == pygame.K_b:
                    pause()
        if lead_x <= 0 or lead_y <= 0 or lead_x >= DISPLAY_WIDTH or lead_y >= DISPLAY_HEIGHT:
            game_over()

        lead_x += lead_x_change
        lead_y += lead_y_change

        GAME_DISPLAY.fill(WHITE)
        pygame.draw.rect(GAME_DISPLAY, RED, [randappleX, randappleY, BLOCK_SIZE, BLOCK_SIZE])
        snake_create(snakelist)
        score(snakelength - 1)
        pygame.display.update()
        snakelist.append([lead_x, lead_y])
        if snakelength < len(snakelist):
            del(snakelist[0])

        if lead_x == randappleX and lead_y == randappleY:
            randappleX, randappleY = apple_create()
            snakelength += 1

        CLOCK.tick(FPS)

    quit_game()


if __name__ == '__main__':
    pygame.init()
    GAME_DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('snake game')
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont(None, 35)
    LFONT = pygame.font.SysFont(None, 75)
    BACKGROUND_IMAGE = pygame.image.load("snake.png")
    PAUSE_IMAGE = pygame.image.load("pause.jpg")
    intro()
