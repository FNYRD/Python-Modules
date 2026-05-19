from ex0.CreatureFactory import CreatureFactory
from ex0.Creature import Creature
from ex1.Shiftling import Shiftling
from ex1.Morphagon import Morphagon


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
