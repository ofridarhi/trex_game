import pygame
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

FPS = 120

WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 10
ROWS = WIDTH // SQUARE_SIZE
COLS = HEIGHT // SQUARE_SIZE
PADDING = 2

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")

DIRECTION_DICT = dict()
DIRECTION_DICT['right'] = (1, 0)
DIRECTION_DICT['left'] = (-1, 0)
DIRECTION_DICT['up'] = (0, -1)
DIRECTION_DICT['down'] = (0, 1)

list_of_snake_squares = []
count = 0


class Board:
    def __init__(self):
        self.clear_board()

    def clear_board(self):
        WIN.fill(WHITE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(WIN, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), PADDING)
                pygame.display.update()


class Snake_body:
    def __init__(self):
        self.x = SQUARE_SIZE * 5 + PADDING
        self.y = SQUARE_SIZE * 5 + PADDING
        self.x_vel = SQUARE_SIZE
        self.y_vel = SQUARE_SIZE
        self.color = GREEN
        self.width = SQUARE_SIZE - PADDING * 2
        self.height = SQUARE_SIZE - PADDING * 2
        self.direction = DIRECTION_DICT['right']
        self.snake_cells = [(self.x, self.y)]
        self.head = False

    def add_snake(self, list_of_snake, count):
        list_of_snake.append(Snake_body().snake_cells)
        count += 1
        self.draw()

    def draw(self):
        pygame.draw.rect(WIN,self.color,(self.x,self.y,self.width,self.height))
        pygame.display.update()

    def change_snake_direction(self):
        time.sleep(0.2)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = DIRECTION_DICT['up']
        elif keys[pygame.K_DOWN]:
            self.direction = DIRECTION_DICT['down']
        elif keys[pygame.K_LEFT]:
            self.direction = DIRECTION_DICT['left']
        elif keys[pygame.K_RIGHT]:
            self.direction = DIRECTION_DICT['right']
        print('test')

    def is_head(self):
        pass

    def change_snake_head_direction(self):
        pass


def main():
    board = Board()
    clock = pygame.time.Clock()
    snake = Snake_body()
    run = True
    while run:
        clock.tick(FPS)
        snake.add_snake(list_of_snake_squares,count)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            snake.direction += DIRECTION_DICT['up']
            print("test")
        elif keys[pygame.K_DOWN]:
            snake.direction = DIRECTION_DICT['down']
        elif keys[pygame.K_LEFT]:
            snake.direction = DIRECTION_DICT['left']
        elif keys[pygame.K_RIGHT]:
            snake.direction = DIRECTION_DICT['right']
        direction_x, direction_y = self.direction
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # if event.type == pygame.KEYUP


if __name__ == '__main__':
    main()
