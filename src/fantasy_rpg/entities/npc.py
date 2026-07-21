from dataclasses import dataclass
from fantasy_rpg.entities.entity import Entity
from fantasy_rpg.world.tile import Tile


@dataclass
class NPC(Entity):
    dialogue: list[str]
    quests: list