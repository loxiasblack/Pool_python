from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    @abstractmethod
    def create_creature(self, name_or_power=None) -> Card:
        """Factory method for creatures"""
        pass

    @abstractmethod
    def create_spell(self, name_or_power=None) -> Card:
        """Factory method for spells"""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power=None) -> Card:
        """Factory method for artifacts"""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """Creates a full deck with theme consistency"""
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """Returns what card types this factory supports"""
        pass
