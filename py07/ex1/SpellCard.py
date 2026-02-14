from ex0.Card import Card
from ex0.CreatureCard import CreatureCard

class SpellCard(Card):
    """
    Docstring for SpellCard
    """
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str) -> None:
        """
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """
        """
        try:
            mana_available = game_state['mana_available']

            if self.is_playable(mana_available):
                return {
                    'card_played': self.name,
                    'mana_used': self.cost,
                    'effect': self.effect_type
                }
            return {}
        except KeyError:
            return {}

    def resolve_effect(self, targets: list[CreatureCard]) -> dict:
        """
        """
        if "damage" in self.effect_type:
            list_of_elements = self.effect_type.split(' ')
            for element in list_of_elements:
                try:
                    damage = int(element)
                    break
                except ValueError:
                    continue
            for target in targets:
                target.health
        return {}
