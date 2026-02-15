from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import Card, CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import List


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List[Card], battlefield: List[Card]) -> dict:
        """
        Logic:
        - Play cheapest creatures first (build board)
        - Use spells to remove enemy threats
        - Attack with all available creatures
        - Prioritize face damage over trading
        """
        actions = {
            "cards_played": [],
            "mana_used": 0,
            "targets_attacked": [],
            "damage_dealt": 0,
        }
        available_mana = 10  # i will assume that each turn
        sorted_hand = sorted(hand, key=lambda card: card.cost)

        for card in sorted_hand:
            if card.cost <= available_mana:
                if card.is_playable(available_mana):
                    actions["cards_played"].append(card.name)
                    actions["mana_used"] += card.cost
                    available_mana -= card.cost

                if isinstance(card, (CreatureCard, ArtifactCard)):
                    battlefield.append(card)
                if isinstance(card, SpellCard):
                    spell_damage = 3
                    actions["damage_dealt"] += spell_damage
                    actions["targets_attacked"].append("Enemy with spell")

        for card in battlefield:
            if isinstance(card, CreatureCard):
                target = "Enemy"
                damage = card.attack
                actions["targets_attacked"].append(target)
                actions["damage_dealt"] += damage
        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(
        self, available_targets: list[CreatureCard]
    ) -> list:
        """
        Logic:
        - Player face > low health creatures > high health creatures
        """
        sorted_targets = sorted(available_targets, key=lambda t: t.health)
        return sorted_targets
