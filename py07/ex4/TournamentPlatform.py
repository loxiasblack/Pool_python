from ex4.TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform:

    def __init__(self):
        self.registered_card: Dict[TournamentCard] = {}
        self.match_history: List[dict] = []
        self.total_matches = 0

    def register_card(self, card: TournamentCard) -> str:
        card_id = (
            f"{card.name.capitalize()}_{len(self.registered_card) + 1:03d}"
        )
        self.registered_card[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        try:
            card1: TournamentCard = self.registered_card[card1_id]
        except KeyError:
            raise NameError("The card is not registred")
        try:
            card2: TournamentCard = self.registered_card[card2_id]
        except KeyError:
            raise NameError("The card is not registred")
        if not card1 or not card2:
            return {"error": "Card not found"}
        power1 = card1.damage + card1.health
        power2 = card2.damage + card2.health

        if power1 > power2:
            winner_id = card1_id
            loser_id = card2_id
            card1.update_wins(1)
            card2.update_losses(1)
        else:
            winner_id = card2_id
            loser_id = card1_id
            card2.update_wins(1)
            card1.update_losses(1)
        match_result = {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": self.registered_card[winner_id].elo,
            "loser_rating": self.registered_card[loser_id].elo,
        }
        self.match_history.append(match_result)
        self.total_matches += 1
        return match_result

    def get_leaderboard(self) -> list:
        leaderbord = []
        for card_id, card in self.registered_card.items():
            rank_info = card.get_rank_info()
            rank_info["card_id"] = card_id
            leaderbord.append(rank_info)
        leaderbord.sort(key=lambda x: x["rating"], reverse=True)
        return leaderbord

    def generate_tournament_report(self) -> dict:
        if not self.registered_card:
            return {"error": "No cards registred"}
        total_cards = len(self.registered_card)
        total_maches = self.total_matches

        ratings = [card.elo for card in self.registered_card.values()]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        leaderboard = self.get_leaderboard()
        top_card = leaderboard[0] if leaderboard else None

        return {
            "total_cards": total_cards,
            "matches_played": total_maches,
            "avg_ratings": round(avg_rating, 2),
            "top_cards": top_card["name"],
            "platform_status": "active",
        }
