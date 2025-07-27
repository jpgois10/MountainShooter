from code.EnemyShot import EnemyShot
from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_entity(entity1, entity2):
        valid_interaction = False
        if isinstance(entity1, Enemy) and isinstance(entity2, PlayerShot):
            valid_interaction = True
        elif isinstance(entity1, PlayerShot) and isinstance(entity2, Enemy):
            valid_interaction = True
        elif isinstance(entity1, Player) and isinstance(entity2, EnemyShot):
            valid_interaction = True
        elif isinstance(entity1, EnemyShot) and isinstance(entity2, Player):
            valid_interaction = True

        if valid_interaction:
            if (entity1.rect.right >= entity2.rect.left and
                    entity1.rect.left <= entity2.rect.right and
                    entity1.rect.bottom >= entity2.rect.top and
                    entity1.rect.top <= entity2.rect.bottom):
                entity1.health -= entity2.damage
                entity2.health -= entity1.damage
                entity1.last_dmg = entity2.name
                entity2.last_dmg = entity1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'PlayerShot':
            for entity in entity_list:
                if entity.name == 'Player':
                    entity.score += enemy.score

    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right <= 0:
                entity.health = 0
        if isinstance(entity, PlayerShot):
            if entity.rect.left >= WIN_WIDTH:
                entity.health = 0
        if isinstance(entity, EnemyShot):
            if entity.rect.right <= 0:
                entity.health = 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for entity in entity_list:
            if entity.health <= 0:
                if isinstance(entity, Enemy):
                    EntityMediator.__give_score(entity, entity_list)
                entity_list.remove(entity)

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)
