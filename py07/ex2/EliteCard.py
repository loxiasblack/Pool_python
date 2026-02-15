from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        damage: int,
        health: int,
        shield: int,
        combat_type: str,
    ):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.shield = shield
        self.combat_type = combat_type

    def play(self, game_state: dict) -> dict:
        try:
            type = game_state["type"]
            if type == "spell":
                spell = type["spell_name"]
                targets = type["targets"]
                game = self.cast_spell(spell, targets)
            elif type == "chanell":
                amount = game_state["amount"]
                game = self.channel_mana(amount)
            elif type["type"] == "attack":
                target = type["target"]
                game = self.attack(target)
            elif type["type"] == "defend":
                incoming_damage = game_state["damage"]
                game = self.defend(incoming_damage)
            return game
        except KeyError:
            return {}

    def get_combat_stats(self):
        return {
            "card_name": self.name,
            "mana_used": self.cost,
            "type_of_combat": self.combat_type,
            "still_alive": self.health > 0,
        }

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.damage,
            "combat_type": self.combat_type,
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage - self.shield
        self.health -= damage_taken
        still_alive = self.health > 0
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": self.shield,
            "still_alive": still_alive,
        }

    def cast_spell(self, spell_name: str, targets: List) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost,
        }

    def channel_mana(self, amount: int) -> dict:
        self.cost += amount
        return {"channeld": amount, "total_mana": self.cost}

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.cost,
            "ability": self.name,
            "combat_type": self.combat_type,
        }
