import pygame

pygame.init()

WIDTH = 1280
HEIGTH = 720
FPS = 60
clock = pygame.time.Clock()

MAX_ROWS = 30
MAX_COLS = 50
TILE_SIZE = 21

# images laoded
PROPERTY = pygame.image.load('images/property.png')
BACKGROUND = pygame.image.load('images/background.png')

# Load sprite sheet (animation)
sprite_sheet = pygame.image.load("images/loading.png")

LOAD = pygame.image.load('images/laod.png')
NEW = pygame.image.load('images/new.png')
SET = pygame.image.load('images/settings.png')
LOGO = pygame.image.load('images/logo.png')
SIDE = pygame.image.load('images/side.png')
BOTTOM = pygame.image.load('images/bottom.png')
BOX = pygame.image.load('images/box.png')
S_BOX = pygame.image.load('images/s_box.png')
SAVE = pygame.image.load('images/save.png')
SAVE2 = pygame.image.load('images/save2.png')
LOAD2 = pygame.image.load('images/load2.png')
MENU = pygame.image.load('images/menu.png')
MENU1 = pygame.image.load('images/menu1.png')
MENU2 = pygame.image.load('images/menu2.png')
MENU3 = pygame.image.load('images/menu3.png')
MENU4 = pygame.image.load('images/menu4.png')
LAYER = pygame.image.load('images/layer.png')

LAYERS = {
    "LAYER1": pygame.image.load('images/layer1.png'),
    "LAYER1S": pygame.image.load('images/layer1s.png'),
    "LAYER2": pygame.image.load('images/layer2.png'),
    "LAYER2S": pygame.image.load('images/layer2s.png'),
    "LAYER3": pygame.image.load('images/layer3.png'),
    "LAYER3S": pygame.image.load('images/layer3s.png'),
    "LAYER4": pygame.image.load('images/layer4.png'),
    "LAYER4S": pygame.image.load('images/layer4s.png'),
    "LAYER5": pygame.image.load('images/layer5.png'),
    "LAYER5S": pygame.image.load('images/layer5s.png'),
    "LAYER6": pygame.image.load('images/layer6.png'),
    "LAYER6S": pygame.image.load('images/layer6s.png'),
    "LAYER7": pygame.image.load('images/layer7.png'),
    "LAYER7S": pygame.image.load('images/layer7s.png'),
    "LAYER8": pygame.image.load('images/layer8.png'),
    "LAYER8S": pygame.image.load('images/layer8s.png'),
    "LAYER9": pygame.image.load('images/layer9.png'),
    "LAYER9S": pygame.image.load('images/layer9s.png'),
    "LAYER10": pygame.image.load('images/layer10.png'),
    "LAYER10S": pygame.image.load('images/layer10s.png')
}



# colors

E_ORANGE = (255, 157, 0)


# default locations
IMAGE_LOCATION = '../output/images'
OUTPUT_LOCATION = 'output'