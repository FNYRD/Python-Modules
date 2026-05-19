from ex0.CreatureFactory import CreatureFactory
from ex0.Creature import Creature
from ex0.Aquabub import Aquabub
from ex0.Torragon import Torragon


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
