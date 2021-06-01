from .observer import Observer


class AlarmObserver(Observer):
    def __init__(self, parent):
        self.parent = parent

    def update_from_subscreen(self, msg: dict) -> None:
        self.parent.update_from_subscreen(msg)
