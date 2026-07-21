from dataclasses import dataclass

@dataclass
class Spell:
    name: str
    description: str
    requirements: list
    cost: list