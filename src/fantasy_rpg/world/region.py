from dataclasses import dataclass

@dataclass
class Region:
    name: str
    encounters: list
    danger_lvl: int