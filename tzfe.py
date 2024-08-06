import pygame
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_SIZE = 20
BRICK_WIDTH, BRICK_HEIGHT = 75, 30
BRICK_ROWS, BRICK_COLS = 5, 8
PADDLE_SPEED = 15
BALL_SPEED_X, BALL_SPEED_Y = 5, -5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tile shoter")

def draw_bricks(bricks):
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

def main():
    clock = pygame.time.Clock()

    paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_speed = PADDLE_SPEED

    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
    ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            brick = pygame.Rect(col * (BRICK_WIDTH + 10) + 30, row * (BRICK_HEIGHT + 10) + 30, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append(brick)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += paddle_speed

        ball.x += ball_dx
        ball.y += ball_dy

        if ball.left <= 0 or ball.right >= WIDTH:
            ball_dx = -ball_dx
        if ball.top <= 0:
            ball_dy = -ball_dy
        if ball.bottom >= HEIGHT:
            pygame.time.delay(500)  
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

       
        if ball.colliderect(paddle):
            ball_dy = -ball_dy

       
        for brick in bricks:
            if ball.colliderect(brick):
                ball_dy = -ball_dy
                bricks.remove(brick)
                break  

        if not bricks:
            print("You win!")
            pygame.time.delay(2000) 
            running = False

      
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.ellipse(screen, GREEN, ball)
        draw_bricks(bricks)
        pygame.display.flip()
        clock.tick(60)  

    pygame.quit()

if __name__ == "__main__":
    main()

