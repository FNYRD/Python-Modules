from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self) -> None:
        # Persistent state: tracks whether the creature is transformed
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
