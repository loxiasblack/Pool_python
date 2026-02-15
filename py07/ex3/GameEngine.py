from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []
        self.turns_played = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """
        Logic:
        - Set the factory (determines card theme)
        - Set the strategy (determines playstyle)
        - Initialize starting hand from factory
        """
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            factory.create_creature("goblin"),
            factory.create_spell("fireball"),
            factory.create_creature("dragon"),
            factory.create_artifact("mana_ring"),
        ]

    def simulate_turn(self) -> dict:
        """
        Logic:
        1. Use strategy.execute_turn() to decide actions
        2. Use factory-created cards from hand
        3. Apply combat results
        4. Return turn summary
        """
        result = self.strategy.execute_turn(self.hand, self.battlefield)

        for card_name in result["cards_played"]:
            self.hand = [c for c in self.hand if c.name != card_name]

        self.turns_played += 1
        return {
            "startegy": self.strategy.get_strategy_name(),
            "actions": result,
            "hand_remaining": len(self.hand),
            "battelefied_size": len(self.battlefield),
        }

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_played,
            "strategy_used": self.strategy.get_strategy_name(),
            "factory_used": self.factory.__class__.__name__,
            "hand_size": len(self.hand),
            "battlefield_size": len(self.battlefield),
        }
