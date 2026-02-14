from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main():
    print("Building deck with different card types...")
    list_of_cards = [
        CreatureCard('Fire Dragon', 5, "Legendary", 7, 5),
        ArtifactCard('Mana Crystal', 4, 'Normal', 99999, 'Permanent: +1 mana per turn'),
        SpellCard(' Lightning Bol', 3, 'Legenday', 'Deal 3 damage to target')
    ]

    deck_builder = Deck()
    for card in list_of_cards: 
        deck_builder.add_card(card)
    
    stats = deck_builder.get_deck_stats()
    print(f"Deck stats: {stats}\n")

    deck_builder.shuffle()
    print("Drawing and playing cards:\n")
    for x in range(3):
        card = deck_builder.draw_card()
        types = {
            "CreatureCard": "Creature",
            "SpellCard": "Spell",
            "ArtifactCard": "Artifact"
        }
        print(f"Drew: {card.name} ({types[card.__class__.__name__]})")
        game_stat = {
            'mana_available': 9,
            'effect': 'Creature summoned to battlefield'
        }
        print(f"Play result: {card.play(game_stat)}\n")
    
        print("Polymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
    main()
