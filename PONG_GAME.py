import pygame
import sys

pygame.init()
fps = pygame.time.Clock()

# defining colors
white = (255, 255, 255)
black = (0, 0, 0)
bg_color = (71, 103, 107)

# setting up screen
screen_w = 1200
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))

# caption
pygame.display.set_caption("pong")

# creating paddles and ball
paddle_w = 25
paddle_h = 120
ball_r = 15
paddle_l = pygame.Rect(((0 + paddle_w/2)-5), (screen_h/2 - paddle_h/2), paddle_w, paddle_h)
paddle_r = pygame.Rect(((screen_w - paddle_w*2)+15), (screen_h/2 - paddle_h/2), paddle_w, paddle_h)
ball = pygame.Rect((screen_w/2 - ball_r/2), (screen_h/2 - ball_r/2), ball_r, ball_r)

ball_coordinates = [screen_w/2 - ball_r/2, screen_h/2 - ball_r/2]
paddle_l_coordinates = (0 + paddle_w), (screen_h/2 - paddle_h/2)
paddle_r_coordinates = (screen_w - paddle_w*2), (screen_h/2 - paddle_h/2)

# defining speeds
paddle_velocity = 10
ball_velocity_x = 11
ball_velocity_y = 11
ball_velocity = [ball_velocity_x, ball_velocity_y]

# score initialization
l_score = 0
r_score = 0


# game loop
def game_loop():
    global ball_velocity_x, ball_velocity_y, l_score, r_score
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        # adding bg color
        screen.fill(bg_color)

        # drawing every element
        pygame.draw.rect(screen, white, paddle_l)
        pygame.draw.rect(screen, white, paddle_r)
        pygame.draw.circle(screen, white, ball.center, ball_r)

        # move paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_l.move_ip(0, -paddle_velocity)
        if keys[pygame.K_s]:
            paddle_l.move_ip(0, paddle_velocity)
        if keys[pygame.K_UP]:
            paddle_r.move_ip(0, -paddle_velocity)
        if keys[pygame.K_DOWN]:
            paddle_r.move_ip(0, paddle_velocity)

        # move ball
        ball.move_ip(ball_velocity_x, ball_velocity_y)

        # collisions with boundaries
        if ball.top <= 0 + ball_r or ball.bottom >= screen_h - ball_r:
            ball_velocity_y = -ball_velocity_y
        if ball.left <= 0 + ball_r or ball.right >= screen_w - ball_r:
            ball_velocity_x = -ball_velocity_x

        # check collision with left paddle
        if ball.colliderect(paddle_l):
            ball_velocity_x = -ball_velocity_x  # reverse the x velocity

        # check collision with right paddle
        if ball.colliderect(paddle_r):
            ball_velocity_x = -ball_velocity_x  # reverse the x velocity

        # if ball collides with left side, right paddle player gets a point
        if ball.left <= 0 + ball_r:
            r_score += 1
        # if ball collides with right side, left paddle player gets a point
        if ball.right >= screen_w - ball_r:
            l_score +=1 
        
        # drawing score
        font = pygame.font.Font(None, 80)
        score_display = font.render("{} - {}".format(l_score, r_score), True, black)
        screen.blit(score_display, (screen_w/2 - score_display.get_width()/2, 10))
        text_display = font.render("First to five wins!", True, black)
        screen.blit(text_display, (screen_w/2 - text_display.get_width()/2, 55))
        
        if l_score >= 5 or r_score >= 5:
            if l_score >= 5:
                ball.center = (screen_w/2 - ball_r/2, screen_h - ball_r*2)
                ball_velocity_x = 0
                ball_velocity_y = 0
                left_win = font.render("Player on the left wins!", True, black)
                screen.blit(left_win, (screen_w/2 - left_win.get_width()/2, screen_h/2))
            if r_score >= 5:
                ball.center = (screen_w/2 - ball_r/2, screen_h - ball_r*2)
                ball_velocity_x = 0
                ball_velocity_y = 0
                right_win = font.render("Player on the right wins!", True, black)
                screen.blit(right_win, (screen_w/2 - right_win.get_width()/2, screen_h/2))

        # update display
        pygame.display.flip()

        # control fps
        pygame.time.Clock().tick(60)
        
# call game loop
game_loop()