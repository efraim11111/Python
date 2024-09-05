import random
import sys
import time
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 400
PADDLE_RADIUS = 20
PUCK_RADIUS = 10
PADDLE_SPEED = 5
PUCK_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GOAL_WIDTH = 100
WINNING_SCORE = 5
GAME_TIME = 60
COOLDOWN_TIME = 0.02

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Air Hockey')

paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_RADIUS, PADDLE_RADIUS * 2, PADDLE_RADIUS * 2)
paddle2 = pygame.Rect(WIDTH - 70, HEIGHT // 2 - PADDLE_RADIUS, PADDLE_RADIUS * 2, PADDLE_RADIUS * 2)
puck = pygame.Rect(WIDTH // 2 - PUCK_RADIUS, HEIGHT // 2 - PUCK_RADIUS, PUCK_RADIUS * 2, PUCK_RADIUS * 2)
puck_dx, puck_dy = PUCK_SPEED, PUCK_SPEED

goal1 = pygame.Rect(0, HEIGHT // 2 - GOAL_WIDTH // 2, 10, GOAL_WIDTH)
goal2 = pygame.Rect(WIDTH - 10, HEIGHT // 2 - GOAL_WIDTH // 2, 10, GOAL_WIDTH)

score1 = 0
score2 = 0
start_time = pygame.time.get_ticks()

last_collision_time = 0


def draw_objects():
    screen.fill(WHITE)
    pygame.draw.ellipse(screen, BLACK, paddle1)
    pygame.draw.ellipse(screen, BLACK, paddle2)
    pygame.draw.ellipse(screen, BLUE, puck)
    pygame.draw.rect(screen, BLACK, goal1)
    pygame.draw.rect(screen, BLACK, goal2)

    font = pygame.font.SysFont(None, 36)
    text1 = font.render(f'Player 1: {score1}', True, BLACK)
    text2 = font.render(f'Player 2: {score2}', True, BLACK)
    screen.blit(text1, (20, 20))
    screen.blit(text2, (WIDTH - 150, 20))

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    remaining_time = max(GAME_TIME - int(elapsed_time), 0)
    timer_text = font.render(f'Time: {remaining_time}', True, BLACK)
    screen.blit(timer_text, (WIDTH // 2 - 50, 20))

    pygame.display.flip()


def handle_collision():
    global puck_dx, puck_dy, score1, score2, last_collision_time

    current_time = time.time()
    if (current_time - last_collision_time) < COOLDOWN_TIME:
        return

    if puck.colliderect(paddle1):
        puck.right = paddle1.left
        puck_dx = -puck_dx
        puck_dy += (paddle1.dy if hasattr(paddle1, 'dy') else 0)
        last_collision_time = time.time()

    if puck.colliderect(paddle2):
        puck.left = paddle2.right
        puck_dx = -puck_dx
        puck_dy += (paddle2.dy if hasattr(paddle2, 'dy') else 0)
        last_collision_time = time.time()

    # Collide with goals
    if puck.colliderect(goal1):
        score2 += 1
        reset_puck()
        reset_paddle()
    if puck.colliderect(goal2):
        score1 += 1
        reset_puck()
        reset_paddle()

    if puck.left <= 0 or puck.right >= WIDTH:
        puck_dx = -puck_dx

    if puck.top <= 0 or puck.bottom >= HEIGHT:
        puck_dy = -puck_dy


def reset_puck():
    global puck_dx, puck_dy
    puck.x = WIDTH // 2 - PUCK_RADIUS
    puck.y = HEIGHT // 2 - PUCK_RADIUS
    puck_dx = random.choice([-PUCK_SPEED, PUCK_SPEED])
    puck_dy = random.choice([-PUCK_SPEED, PUCK_SPEED])


def reset_paddle():
    paddle2.x = PADDLE_SPEED * 3
    paddle2.y = HEIGHT // 2 - PADDLE_RADIUS
    paddle1.x = WIDTH - PADDLE_RADIUS * 3
    paddle1.y = HEIGHT // 2 - PADDLE_RADIUS


def display_winner(winner):
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 72)
    text = font.render(f'{winner} Wins!', True, BLACK)
    screen.blit(text, (WIDTH // 4, HEIGHT // 3))
    pygame.display.flip()
    with open("game_result.txt", "w") as file:
        file.write(f'{winner} Wins!')
    pygame.time.wait(2000)


def game_loop():
    global puck_dx, puck_dy

    clock = pygame.time.Clock()
    reset_paddle()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        handle_collision()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += PADDLE_SPEED
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y += PADDLE_SPEED
        if keys[pygame.K_a] and paddle1.left > 0:
            paddle1.x -= PADDLE_SPEED
        if keys[pygame.K_d] and paddle1.right < WIDTH:
            paddle1.x += PADDLE_SPEED
        if keys[pygame.K_LEFT] and paddle2.left < WIDTH:
            paddle2.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle2.right < WIDTH:
            paddle2.x += PADDLE_SPEED

        puck.x += puck_dx
        puck.y += puck_dy

        draw_objects()

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        remaining_time = max(GAME_TIME - int(elapsed_time), 0)

        if score1 > score2 + 2:
            display_winner("Player 1")
            break
        if score2 > score1 + 2:
            display_winner("Player 2")
            break
        if remaining_time == 0:
            if score1 > score2:
                display_winner("Player 1")
            elif score2 > score1:
                display_winner("Player 2")
            else:
                display_winner("Draw")
            break

        clock.tick(30)


if __name__ == "__main__":
    game_loop()
