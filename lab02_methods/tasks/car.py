class Car:
    """Задача: car"""
    def __init__(self):
        self.speed = 0

    def accelerate(self, v: int):
        pass

    def brake(self, v: int):
        """Снижает скорость, но не ниже 0"""
        if self.speed-v<0:
            self.speed = 0
        else:
            self.speed-=v
