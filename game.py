import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Shooter Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define player attributes
player_size = 50
player_pos = [WIDTH / 2, HEIGHT - player_size * 2]
player_speed = 5

# Define enemy attributes
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
enemy_speed = 5

# Define bullet attributes
bullet_size = 10
bullet_pos = []
bullet_speed = 7

# Define game over flag
game_over = False

# Set up clock for controlling frame rate
clock = pygame.time.Clock()

# Main game loop
while not game_over:

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_speed

            # Fire bullet
            elif event.key == pygame.K_SPACE:
                bullet_pos.append([player_pos[0] + player_size / 2, player_pos[1]])

    # Update enemy position
    for idx, enemy in enumerate(enemy_list):
        if enemy[1] >= 0 and enemy[1] < HEIGHT:
            enemy[1] += enemy_speed
        else:
            enemy_list.pop(idx)

    # Update bullet position
    for idx, bullet in enumerate(bullet_pos):
        if bullet[1] >= 0:
            bullet[1] -= bullet_speed
        else:
            bullet_pos.pop(idx)

    # Collision detection
    for enemy in enemy_list:
        if enemy[1] + enemy_size > player_pos[1]:
            if (enemy[0] >= player_pos[0] and enemy[0] <= player_pos[0] + player_size) or \
                    (player_pos[0] >= enemy[0] and player_pos[0] <= enemy[0] + enemy_size):
                game_over = True

    # Draw everything
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw enemies
    for enemy in enemy_list:
        pygame.draw.rect(screen, (255, 0, 0), (enemy[0], enemy[1], enemy_size, enemy_size))

    # Draw bullets
    for bullet in bullet_pos:
        pygame.draw.rect(screen, (0, 255, 0), (bullet[0], bullet[1], bullet_size, bullet_size))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(30)