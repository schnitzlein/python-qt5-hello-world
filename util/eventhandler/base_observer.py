from .observer import Observer
from .subject import Subject

class BaseObserver(Observer):
    def __init__(self, parent):
        self.parent = parent

    def update_from_subscreen(self, msg: dict) -> None:
        self.parent.update_from_subscreen(msg)
    
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("BaseObserver: Found event which I should react on.")
