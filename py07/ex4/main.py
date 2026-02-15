from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    card_1 = TournamentCard("dragon", 4, "Legendary", 7, 5)
    card_2 = TournamentCard("wizard", 4, "Epic", 4, 8)

    platform = TournamentPlatform()

    dragon_id = platform.register_card(card_1)
    wizard_id = platform.register_card(card_2)
    tournament_card_interfaces = [
        base.__name__ for base in TournamentCard.__bases__
    ]
    print(f"Fire Dragon (ID: {dragon_id})")
    print(f"-Interfaces: {tournament_card_interfaces}")
    print(f"-Rating: {card_1.elo}")
    print(f"-Record: {card_1.wins}-{card_1.loss}\n")

    print(f"Ice Wizard (ID: {wizard_id}):")
    print(f"-Interfaces: {tournament_card_interfaces}")
    print(f"-Rating: {card_2.elo}")
    print(f"-Record: {card_2.wins}-{card_2.loss}\n")

    print("Creating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}\n")

    print("Tournament Leaderboard:")
    leader_bord = platform.get_leaderboard()
    for rank, info in enumerate(leader_bord):
        name = info["name"]
        win = info["wins"]
        loss = info["losses"]
        rank = info["rating"]
        print(f"{rank + 1}. {name} - Ratings: {rank} ({win}-{loss})")

    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(report)
    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously")


if __name__ == "__main__":
    main()
