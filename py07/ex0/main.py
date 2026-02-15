from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"{creature.get_card_info()}\n")
    print("Playing Fire Dragon with 6 mana available:")
    game_state = {
        "mana_available": 6,
        "effect": "Creature summoned to battlefield",
    }
    result = creature.play(game_state)
    if result:
        print(f"Play result: {result}\n")

    print("Fire Dragon attacks Goblin Warrior:")
    Target = CreatureCard("Goblin Warrior", 3, "Lengendary", 6, 5)
    attack = creature.attack_target(Target)
    print(f"Attack result: {attack}\n")

    print("Testing insufficient mana (3 available):")
    game_state = {
        "mana_available": 3,
        "effect": "Creature summoned to battlefield",
    }
    result = creature.play(game_state)
    if result:
        print(f"Play result: {result}\n")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
