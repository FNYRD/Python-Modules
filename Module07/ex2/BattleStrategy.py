from abc import ABC, abstractmethod
from ex0.Creature import Creature


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...
