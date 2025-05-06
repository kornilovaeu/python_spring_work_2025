import pygame

clock = pygame.time.Clock()

#инициализация программы
pygame.init()
screen = pygame.display.set_mode((1024, 512))
pygame.display.set_caption('Hunter and Lion')
icon = pygame.image.load('Images/player_right/player_right1.png')
pygame.display.set_icon(icon)

#Игрок
bg = pygame.image.load('Images/bg_1.png')
walk_left = [
    pygame.image.load('Images/player_left/player_left1.png'),
    pygame.image.load('Images/player_left/player_left2.png'),
    pygame.image.load('Images/player_left/player_left3.png'),
    pygame.image.load('Images/player_left/player_left4.png'),
]
walk_right = [
    pygame.image.load('Images/player_right/player_right1.png'),
    pygame.image.load('Images/player_right/player_right2.png'),
    pygame.image.load('Images/player_right/player_right3.png'),
    pygame.image.load('Images/player_right/player_right4.png'),
]

#Лев
lion = pygame.image.load('Images/lion.png')
lion_list_in_game = []

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 310

is_jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
bg_sound.play()

lion_timer = pygame.USEREVENT + 1
pygame.time.set_timer(lion_timer, 2800)

label = pygame.font.Font('fonts/MasqueradeToyStoreStuff-Regular.ttf', 40)
lose_label = label.render('You lose!', False, (20, 12, 3))

gameplay = True

#основной игровой цикл
running = True
while running:

    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x + 1024, 0))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

        if lion_list_in_game:
            for (i, el) in enumerate(lion_list_in_game):
                screen.blit (lion, el)
                el.x -= 7

                if el.x < -10:
                    lion_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left [player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50 :
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 300:
            player_x += player_speed
#отследить, нажали ли на клавишу ПРОБЕЛ (затем поднимаем/опускаем игрока)
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    player_y -= (jump_count ** 2)
                else:
                    player_y += (jump_count ** 2)
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 7


        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -1024:
            bg_x = 0
    else:
        screen.fill((87, 88, 31))
        screen.blit (lose_label, (400, 250))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == lion_timer:
            lion_list_in_game.append(lion.get_rect(topleft=(1030, 325)))

    clock.tick (10)






