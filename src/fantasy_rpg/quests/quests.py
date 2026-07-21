from dataclasses import dataclass
from fantasy_rpg.world.tile import Tile

@dataclass
class Quest:
    location: Tile
    item_reward: list
    experience: int
    difficulty: str
