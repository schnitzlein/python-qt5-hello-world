from abc import ABC, abstractmethod



class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update_from_subscreen(self, msg: dict) -> None:
        """
        Receive update msg from subject.
        """
        pass
