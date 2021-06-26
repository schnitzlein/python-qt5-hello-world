from abc import ABC, abstractmethod
from random import randrange
from typing import List
from .observer import Observer
from .subject import Subject


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()
    
    def creatingEvents(self) -> None:
        """
        This functions is the high-level function which creates custom events without the QT Framework
        QEvent and Signal system
        With this functions is a call from a sub-class or thread simulated.
        It fires a new event through changeing the current state of the sub-class or thread.
        Each state number can be seen as an Enum and individual Event
        """
        print("\nSubject: I am subscreen or worker thread/process and creating events.")
        self._state = randrange(0, 10)
        print(f"Subject: please handle my Event with state/event_number: {self._state}")
        self.notify()