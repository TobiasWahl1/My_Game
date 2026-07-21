from dataclasses import dataclass
from fantasy_rpg.entities.entity import Entity
from fantasy_rpg.quests.quests import Quest
from fantasy_rpg.items.items import Item
from fantasy_rpg.combat.spells import Spell
from fantasy_rpg.combat.skills import Skill


@dataclass
class Player(Entity):
    inventory: list[Item]
    learned_spells: list[Spell]
    learned_skills: list[Skill]
    quests: list[Quest]