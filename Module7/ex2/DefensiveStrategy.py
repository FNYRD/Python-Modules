from ex0.Creature import Creature
from ex1.HealCapability import HealCapability
from ex2.BattleStrategy import BattleStrategy, InvalidStrategyError


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy"
            )
        # Type is narrowed after the guard above
        assert isinstance(creature, HealCapability)
        print(creature.attack())
        print(creature.heal())
