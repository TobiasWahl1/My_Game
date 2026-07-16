from dataclasses import dataclass
from fantasy_rpg.entities.entity import Entity


@dataclass
class Player(Entity):
    inventory: list
    learned_spells: list
    learned_skills: list
    quests: list