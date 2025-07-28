import random
import pygame

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Enemy import Enemy
from code.EntityMediator import EntityMediator
from code.Const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_ENEMY, COLOR_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name +'Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_ENEMY)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
                if isinstance(entity, (Player, Enemy)):
                    shoot = entity.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                    if entity.name == 'Player':
                        self.level_text(14, f'Player - Health: {entity.health} | Score: {entity.score}', COLOR_GREEN,
                                        (10, 25))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for entity in self.entity_list:
                            if isinstance(entity, Player) and entity.name == 'Player':
                                player_score[0] = entity.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.update()

            # collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
