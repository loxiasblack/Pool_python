from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(
        self, name: str, cost: int, rarity: str, damage: int, health: int
    ):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.wins = 0
        self.loss = 0
        self.elo = 1200

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournement card summoned",
            "rating": self.elo,
        }

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.damage,
            "attacker_rationg": self.elo,
        }

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        survived = self.health > 0
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "health_remaining": max(0, self.health),
            "survived": survived,
        }

    def get_combat_stats(self):
        return {
            "attack": self.damage,
            "health": self.health,
            "pwer_level": self.damage + self.health,
        }

    def calculate_rating(self) -> int:
        win_value = 16
        loss_value = 16
        self.elo = (
            self.elo + (self.wins * win_value) - (self.loss * loss_value)
        )
        return max(0, self.elo)

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses) -> None:
        self.loss += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        total_maches = self.wins + self.loss
        win_rate = (self.wins / total_maches) if total_maches > 0 else 0.0

        return {
            "name": self.name,
            "rating": self.elo,
            "wins": self.wins,
            "losses": self.loss,
            "total_matches": total_maches,
            "winrate": round(win_rate, 2),
        }

    def get_tournament_stats(self) -> dict:
        card_info = self.get_card_info()
        combat_stat = self.get_combat_stats()
        rank_info = self.get_rank_info()

        return {"card": card_info, "combat": combat_stat, "rank": rank_info}
