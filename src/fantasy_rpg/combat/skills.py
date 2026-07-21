from dataclasses import dataclass

@dataclass
class Skill:
    name: str
    description: str
    requirements: list
    cost: list