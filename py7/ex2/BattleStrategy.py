from abc import ABC, abstractmethod
from ex1.Capability import TransformCapability, HealCapability


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature) -> None:
        print(creature.attack())


class AgressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive stategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise Exception(
                f"Invalid Creature '{creature.name}'"
                " for this defensive stategy"
            )
        print(creature.attack())
        print(creature.heal())
