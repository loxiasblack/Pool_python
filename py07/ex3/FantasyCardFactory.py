from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creatures = {
            "dragon": {
                "cost": 5,
                "rarity": "Legendary",
                "attack": 7,
                "health": 5,
            },
            "goblin": {
                "cost": 2,
                "rarity": "Legendary",
                "attack": 2,
                "health": 2,
            },
            "elf": {"cost": 3, "rarity": "Rare", "attack": 3, "health": 3},
            "wizard": {"cost": 4, "rarity": "Epic", "attack": 2, "health": 6},
        }
        self.spells = {
            "fireball": {
                "cost": 3,
                "rarity": "Common",
                "effect_type": "damage",
            },
            "heal": {"cost": 2, "rarity": "Common", "effect_type": "heal"},
            "lightning": {
                "cost": 4,
                "rarity": "Rare",
                "effect_type": "damage",
            },
        }
        self.artifacts = {
            "mana_ring": {
                "cost": 2,
                "rarity": "Rare",
                "durability": 5,
                "effect": "+1 mana",
            },
            "sword": {
                "cost": 3,
                "rarity": "Common",
                "durability": 3,
                "effect": "+1 mana",
            },
            "shield": {
                "cost": 2,
                "rarity": "Common",
                "durability": 4,
                "effect": "+1 mana",
            },
        }

    def create_creature(self, name_or_power: str = None) -> Card:
        if name_or_power is None:
            creature_name = random.choice(list(self.creatures.keys()))
        elif isinstance(name_or_power, str):
            creature_name = name_or_power.lower()
            if creature_name not in self.creatures:
                creature_name = "goblin"
        else:
            raise TypeError(
                "the Name of the creature doesn;t exist in my Factory"
            )
        feature_name = random.choice(["Warior", "Beast", "Chamipon"])
        card_name = f"{creature_name.capitalize()} {feature_name}"
        template = self.creatures[creature_name]

        return CreatureCard(
            name=card_name,
            cost=template["cost"],
            rarity=template["rarity"],
            attack=template["attack"],
            health=template["health"],
        )

    def create_spell(self, name_or_power: str = None) -> Card:
        if name_or_power is None:
            spell_name = random.choice(list(self.spells.keys()))
        elif isinstance(name_or_power, str):
            spell_name = name_or_power.lower()
            if spell_name not in self.spells:
                spell_name = "fireball"
        else:
            raise TypeError("You didnt type a real name")

        template = self.spells[spell_name]

        return SpellCard(
            name=spell_name.capitalize(),
            cost=template["cost"],
            rarity=template["rarity"],
            effect_type=template["effect_type"],
        )

    def create_artifact(self, name_or_power=None) -> Card:
        if name_or_power is None:
            artifact_name = random.choice(list(self.artifacts.keys()))
        elif isinstance(name_or_power, str):
            artifact_name = name_or_power.lower()
            if artifact_name not in self.artifacts:
                artifact_name = "sword"
        else:
            raise TypeError("ONly string in the name of power")

        template = self.artifacts[artifact_name]
        return ArtifactCard(
            name=artifact_name.capitalize(),
            cost=template["cost"],
            rarity=template["rarity"],
            durability=template["durability"],
            effect=template["effect"],
        )

    def create_themed_deck(self, size: int) -> dict:
        """
        Logic:
        - Create balanced mix: 50% creatures, 30% spells, 10% artifacts
        - Use randomness for variety
        """
        deck = {"creatures": [], "spells": [], "artifacts": []}
        num_creatures = int(size * 0.5)
        num_spells = int(size * 0.3)
        num_artifacts = size - num_creatures - num_spells

        for _ in range(num_creatures):
            deck["creatures"].append(self.create_creature())

        for _ in range(num_spells):
            deck["spells"].append(self.create_spell())

        for _ in range(num_artifacts):
            deck["artifacts"].append(self.create_artifact())

        return deck

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self.creatures.keys()),
            "spells": list(self.spells.keys()),
            "artifacts": list(self.artifacts.keys()),
        }
