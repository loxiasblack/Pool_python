from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.FantasyCardFactory import CreatureCard, SpellCard
from ex3.FantasyCardFactory import ArtifactCard
from ex3.AggressiveStrategy import AggressiveStrategy
import random


def main():
    print("=== DataDeck Game Engine ===\n")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    game_engine = GameEngine()
    print("Configuring Fantasy Card Game..")
    game_engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {game_engine.strategy.get_strategy_name()}")
    types = {"creatures": [], "spells": [], "artifact": []}
    for card in game_engine.hand:
        if isinstance(card, CreatureCard):
            types["creatures"].append(card.name)
        elif isinstance(card, SpellCard):
            types["spells"].append(card.name)
        elif isinstance(card, ArtifactCard):
            types["artifact"].append(card.name)

    print(f"Available types: {types}\n")
    print("Simulating aggressive turn...")

    hand = []
    for i in range(3):
        card = random.choice(game_engine.hand)
        hand.append(f"{card.name} ({card.cost})")
    print(f"Hand: {hand}")

    print("Turn execution")
    print(f"{game_engine.strategy.__class__.__name__}")
    print(f"Actions: {strategy.execute_turn(game_engine.hand, [])}\n")
    game_engine.simulate_turn()

    print("Game Report")
    print(f"{game_engine.get_engine_status()}\n")
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
