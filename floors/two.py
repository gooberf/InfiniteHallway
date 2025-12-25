import time
import pygame
# floor 2 is pygame???


def start(inventory):
    print(inventory) if len(inventory) > 0 else print("Inventory is empty.")
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Red Square - WASD movement")
    clock = pygame.time.Clock()
    chest_opened = False
    SQUARE_SIZE = 50
    player = pygame.Rect((WIDTH - SQUARE_SIZE) // 2, (HEIGHT - SQUARE_SIZE) // 2, SQUARE_SIZE, SQUARE_SIZE)
    SPEED = 500  # pixels per second
    chest = pygame.Rect(100, 100, 40, 40)

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        dx = dy = 0
        colliding = player.colliderect(chest)
        if keys[pygame.K_w]:
            dy -= 1
        if keys[pygame.K_s]:
            dy += 1
        if keys[pygame.K_a]:
            dx -= 1
        if keys[pygame.K_d]:
            dx += 1
        if keys[pygame.K_e] and colliding and not chest_opened:
            inventory.append("Gold Coin")
            chest_opened = True
            print("You got a golden coin!")
        # Normalize diagonal speed
        if dx != 0 and dy != 0:
            inv = 0.70710678
            dx *= inv
            dy *= inv

        player.x += int(dx * SPEED * dt)
        player.y += int(dy * SPEED * dt)

        # Keep inside screen
        player.clamp_ip(screen.get_rect())
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.draw.rect(screen, (255, 255, 0), chest) if not chest_opened else pygame.draw.rect(screen, (100, 100, 0), chest)
        pygame.display.flip()
    pygame.quit()

