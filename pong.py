import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_w = 800
screen_h = 700
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100

# Ball dimensions
BALL_WIDTH = 15
BALL_HEIGHT = 15

# Initialize clock
clock = pygame.time.Clock()

# Function to draw paddles
def draw_paddle(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Function to draw ball
def draw_ball(x, y):
    pygame.draw.ellipse(screen, WHITE, (x, y, BALL_WIDTH, BALL_HEIGHT))

# Main game loop
def game_loop():
    # Paddle positions
    player1_y = 250
    player2_y = 250

    # Ball position and velocity
    ball_x = screen_w/2 - BALL_WIDTH/2
    ball_y = screen_h/2 - BALL_HEIGHT/2
    ball_velocity_x = 7
    ball_velocity_y = 7

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Move paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1_y -= 7
        if keys[pygame.K_s]:
            player1_y += 7
        if keys[pygame.K_UP]:
            player2_y -= 7
        if keys[pygame.K_DOWN]:
            player2_y += 7

        # Move ball
        ball_x += ball_velocity_x
        ball_y += ball_velocity_y

        # Ball collision with walls
        if ball_y <= 0 or ball_y >= screen_h-BALL_HEIGHT: 
            ball_velocity_y = -ball_velocity_y

        # Ball collision with paddles
        if ball_x <= 30 and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT:
            ball_velocity_x = -ball_velocity_x
        if ball_x >= 755 and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT:
            ball_velocity_x = -ball_velocity_x

        # Ball out of bounds
        if ball_x <= 0 or ball_x >= 785:
            ball_x = 392
            ball_y = 292
            ball_velocity_x = 7
            ball_velocity_y = 7
        # Clear the screen
        screen.fill(BLACK)

        # Draw paddles and ball
        draw_paddle(15, player1_y)
        draw_paddle(770, player2_y)
        draw_ball(ball_x, ball_y)

        # Update the display
        pygame.display.update()

        # Control the game speed
        clock.tick(60)

# Start the game loop
game_loop()
