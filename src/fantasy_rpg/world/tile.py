from dataclasses import dataclass
from fantasy_rpg.world.region import Region

@dataclass
class Tile:

    x: int
    y: int
    terrain: str
    region: Region
    movement_cost: int = 1
    walkable: bool = True

