class Role:
    def __init__(self, name: str, order: int, passive: bool | None = None):
        self.name = name
        self.order = order
        self.passive = passive

