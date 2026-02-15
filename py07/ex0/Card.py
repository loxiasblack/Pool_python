from abc import ABC, abstractmethod


class Card(ABC):
    """
    Class that represent the blueprint off all Card objects
    in my project
    Attributes:
        name: string representing the name of the Card
        cost: Integer the number of mana to use the Card
        rarity: String representing the rarity of the Card
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Initialisation for the instance of the object with args
        args:
            name:
            cost:
            rarity:
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def play(self, game_state: dict):
        """ABSTRACT METHOD"""
        pass

    abstractmethod(play)

    def get_card_info(self) -> dict:
        """
        Concrete method that show the card information
        return:
            dictionary about card info
        """
        if self.__class__.__name__ == "CreatureCard":
            self.type = "Creature"

        return self.__dict__

    def is_playable(self, available_mana: int) -> bool:
        """
        Instance method to show the ability to play the Card by
        comparing the available_mana with card cost
        args:
            available_mana: integer showing the level of mana
        return:
            True if available mana greater or equal to the card cost
        """
        if available_mana >= self.cost:
            return True
        return False
