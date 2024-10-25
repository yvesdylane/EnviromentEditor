from varaibleEnv import *
from components import Buttons
from components.work_stattion import enviroment

screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("EE🦊️")

running = True
alphaP = 0.
alphaB = 0.
is_blitting = True
chrono = 220 * 10
start_time = 0.
current_time = 0.
waiting = True
let_go = False


load_button = Buttons.Button(142, 335, LOAD, 1)
new_button = Buttons.Button(142, 183, NEW, 1)
settings_button = Buttons.Button(142, 487, SET, 1)
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if is_blitting:
                    alphaP = 255
                elif waiting:
                    waiting = False
                elif not is_blitting and not waiting:
                    alphaB = 255

    screen.fill((180, 180, 180))
    current_time = pygame.time.get_ticks()

    if is_blitting:
        PROPERTY.set_alpha(alphaP)
        if alphaP >= 255:
            is_blitting = False
            start_time = pygame.time.get_ticks()
        elif alphaP < 255:
            alphaP+=5
            screen.blit(PROPERTY, (0, 0))
    elif not is_blitting and waiting:
        if current_time - start_time >= chrono:
            waiting = False
        else:
            screen.blit(PROPERTY, (0, 0))

    if not is_blitting and not waiting:
        BACKGROUND.set_alpha(alphaB)
        if alphaB < 255:
            alphaB += 1.25
        else:
            let_go = True
        screen.blit(BACKGROUND, (0,0 ))

    if let_go:
        new_button.draw(screen)
        if new_button.clicked:
            enviroment(screen)
        load_button.draw(screen)
        settings_button.draw(screen)
    pygame.display.update()

pygame.quit()