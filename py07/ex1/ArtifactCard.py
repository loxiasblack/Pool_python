from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        """ """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        try:
            mana = game_state["mana_available"]
            if self.is_playable(mana):
                return self.activate_ability()
            return {}
        except KeyError:
            return {}

    def activate_ability(self) -> dict:
        return {
            "card_played": self.name,
            "effect": self.effect,
        }
