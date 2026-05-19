from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability
from ex2.BattleStrategy import BattleStrategy, InvalidStrategyError


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy"
            )
        # Type is narrowed after the guard above
        assert isinstance(creature, TransformCapability)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
