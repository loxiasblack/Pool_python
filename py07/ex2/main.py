from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


def main() -> None:

    print("EliteCard capabilities:")
    for object in EliteCard.mro():
        list_of_capabilities = [
            method
            for method in dir(object)
            if not method.startswith("_") and callable(getattr(object, method))
        ]
        if list_of_capabilities and not object.__name__ == "EliteCard":
            print(f"- {object.__name__}: {list_of_capabilities}")

    elit_card = EliteCard("Arcane Warrior", 4, "Legandary", 5, 9, 3, "melee")
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    enemy = CreatureCard("Enemy", 9, "Normal", 3, 2)
    attack_state = elit_card.attack(enemy)
    defense = elit_card.defend(5)
    print("Combat phase:")
    print(f"Attack result: {attack_state}")
    print(f"Deffend result: {defense}\n")

    print("Magic phase:")
    spell = elit_card.cast_spell("FireBall", ["target1", "target2"])
    print(f"Magic phase: {spell}")
    channel = elit_card.channel_mana(amount=3)
    print(f"Mana channell: {channel}\n")
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
