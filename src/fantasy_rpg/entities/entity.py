from dataclasses import dataclass
from fantasy_rpg.entities.stats import Stats
from fantasy_rpg.world.tile import Tile


@dataclass
class Entity:
    name: str
    gender: str
    occupation: str
    level: int
    health: int
    mana: int
    experience: int
    stats: Stats
    location: Tile
    inventory: list