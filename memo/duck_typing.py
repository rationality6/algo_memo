class Duck:
    def quack(self): print("quack")

    def feathers(self): print("feathers")


class Person:
    def quack(self): print("human quack")

    def feathers(self): print("human feathers")


def in_the_forest(duck):
    duck.quack()
    duck.feathers()


def game():
    donald = Duck()
    hyun = Person()
    in_the_forest(donald)
    in_the_forest(hyun)

game()
