from ex0.CreatureFactory import CreatureFactory
from ex0.Creature import Creature
from ex1.Sproutling import Sproutling
from ex1.Bloomelle import Bloomelle


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()
