from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import List
import random


class Deck:
    """ """

    def __init__(self):
        """ """
        self.deck: List[Card] = []
        self.in_hand: List[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Docstring for add_card

        :param card: Description
        :type card: Card
        """
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        """"""
        for card in self.in_hand:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        card = self.deck.pop()
        self.in_hand.append(card)
        return card

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        sum_of_cost = 0
        for card in self.deck:
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, ArtifactCard):
                spells += 1
            elif isinstance(card, SpellCard):
                artifacts += 1
            sum_of_cost += card.cost
        avg_cost = f"{sum_of_cost / len(self.deck):.1f}"

        return {
            "total_cards": len(self.deck),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
