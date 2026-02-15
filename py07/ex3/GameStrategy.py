from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """Decides what actions to take during a turn"""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Returns the name of this strategy"""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """Orders targets by priority"""
        pass
