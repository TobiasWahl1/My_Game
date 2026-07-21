from dataclasses import dataclass
from fantasy_rpg.entities.entity import Entity
from fantasy_rpg.world.tile import Tile
from fantasy_rpg.items.items import Item

@dataclass
class Enemy(Entity):
    loot: list[Item]