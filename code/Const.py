import pygame

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# E
EVENT_TIMEOUT = pygame.USEREVENT + 2
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player': 3,
    'Enemy1': 2,
    'Enemy2': 1
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player': 100,
    'Enemy1': 40,
    'Enemy2': 60
}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# S
SPAWN_ENEMY = 3000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324


