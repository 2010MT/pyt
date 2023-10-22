import Pygame
import random

# تنظیمات بازی
WIDTH = 800
HEIGHT = 600
FPS = 60

# تنظیم رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# مقدار اولیه‌ی بازی
player_pos = [WIDTH // 2, HEIGHT - 100]
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]

# شروع بازی
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# حلقه‌ی اصلی بازی
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= 50
            elif event.key == pygame.K_RIGHT:
                x += 50
            player_pos[0] = x

    screen.fill(BLACK)

    # حرکت دشمن
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += 10
        else:
            enemy_list.pop(idx)

    # اضافه کردن دشمن جدید
    if len(enemy_list) < 10:
        enemy_size = 50
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
        enemy_list.append(enemy_pos)

    # نمایش دشمن‌ها
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, WHITE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # نمایش ماشین
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], 50, 100))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()