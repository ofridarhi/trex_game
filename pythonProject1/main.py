import random
import time
import pygame

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

WIDTH,HEIGHT = 800,800
SQUARE_SIZE = 25
food_size = 10
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
VEL = SQUARE_SIZE

def create_food():
    random_x = random.randrange(0, WIDTH - SQUARE_SIZE, SQUARE_SIZE)
    random_y = random.randrange(0,HEIGHT - SQUARE_SIZE,SQUARE_SIZE)
    pygame.draw.rect(WIN,GREEN,(random_x, random_y,SQUARE_SIZE,SQUARE_SIZE))
    return random_x,random_y

def new_game():
    pygame.display.set_caption('snake')

    pygame.draw.rect(WIN,WHITE,(WIDTH/2, HEIGHT/2,SQUARE_SIZE,SQUARE_SIZE))

    food_x, food_y = create_food()
    pygame.display.update()
    return food_x,food_y


def move_snake(x,y):
    time.sleep(0.05)
    x_change, y_change = 0, 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        x_change = 0
        y_change = -SQUARE_SIZE
    elif keys[pygame.K_DOWN]:
        x_change = 0
        y_change = SQUARE_SIZE
    elif keys[pygame.K_LEFT]:
        x_change = -SQUARE_SIZE
        y_change = 0
    elif keys[pygame.K_RIGHT]:
        x_change = SQUARE_SIZE
        y_change = 0

    pygame.draw.rect(WIN, BLACK, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    x += x_change
    y += y_change
    pygame.draw.rect(WIN, BLACK, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(WIN, WHITE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    pygame.display.update()
    return x,y

def eat(player_score,x,y):
        player_score += 1
        print(player_score)
        return player_score
def get_over():
    pygame.font.init()
    size = 120
    font = pygame.font.SysFont('freesansbold.ttf', size)
    messege = 'Game over'
    text = font.render(messege, True, GREEN)
    textRect = text.get_rect()
    messege_length = len(messege) * size //2.5
    textRect.center = ((WIDTH - messege_length) // 2, HEIGHT // 4)
    WIN.blit(text,textRect.center)
    pygame.display.update()

    while True:
        answer = input('press c to continue or player s to stop')
        if answer == 'c':
            pass
        elif answer == 's':
            return breakpoint()
        else:
            print('type a valid option')
        print('hi')

def is_out_of_border(x,y):
    if x == WIDTH or x == -SQUARE_SIZE or y == -SQUARE_SIZE or y == HEIGHT:
        get_over()


def main():
    clock = pygame.time.Clock()
    clock.tick(30)
    food_x, food_y = new_game()
    run = True
    x, y = WIDTH / 2, HEIGHT / 2
    player_score = 0
    while run:
        x,y = move_snake(x,y)
        pygame.draw.rect(WIN, BLACK, (x - x_vel, y - y_vel, SQUARE_SIZE, SQUARE_SIZE))
        if x == food_x and y == food_y:
            old_player_score = player_score
            player_score = eat(player_score,x,y)
            if player_score <= old_player_score:
                pygame.draw.rect(WIN, WHITE, (x- x_vel, y - y_vel, SQUARE_SIZE, SQUARE_SIZE))
            food_x, food_y = create_food()
        is_out_of_border(x,y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
if __name__ == '__main__':
    main()