import physics

class test:
    def __init__(self):
        self.rect1 = physics.DynamicRect(0, 0, 10, 10)
        self.rect2 = physics.StaticRect(5, 5, 10, 10)
        self.rect3 = physics.KinematicRect(10, 10, 10, 10)

    def run(self):
        print("Testing DynamicRect:", self.rect1)
        print("Testing StaticRect:", self.rect2)
        print("Testing KinematicRect:", self.rect3)

if __name__ == "__main__":
    test_instance = test()
    test_instance.run()