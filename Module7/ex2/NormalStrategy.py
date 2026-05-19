from ex0.Creature import Creature
from ex2.BattleStrategy import BattleStrategy


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())
