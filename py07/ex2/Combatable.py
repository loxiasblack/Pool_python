from abc import ABC, abstractmethod
from typing import List
from ex0.Card import Card


class Combatable(ABC):
    """class Combatable that will be
    Interface of other cards
    """

    @abstractmethod
    def attack(self, target: List[Card]) -> None:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
