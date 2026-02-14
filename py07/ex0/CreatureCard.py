from ex0.Card import Card

class CreatureCard(Card):
    """
        CreatureCard class inherit from Card abstract base class

    """
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        """
        """
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
    
    def play(self, game_state: dict) -> dict:
        """
            Create Play method to show overiding
        """
        try:
            mana_available = game_state['mana_available']
            effect = game_state['effect']
            is_playable = self.is_playable(mana_available)
            print(f"Playable: {is_playable}")
            if is_playable:
                return {
                    'card_player': self.name,
                    'mana_used': self.cost,
                    'effect': effect
                }
            return {}
        except KeyError:
            return {}

    def attack_target(self, target: Card) -> dict:
        combat_result = self.attack >= target.health
        return {
            'attacker': self.name,
            'target': target.name,
            'damage_dealt': self.attack,
            'combat_resolved': combat_result
        }

