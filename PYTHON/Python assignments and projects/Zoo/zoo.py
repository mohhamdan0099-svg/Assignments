class Animal:

    def __init__(
        self, animal_name, age=1, health_level=100, happines_level=100
    ):
        self.name = animal_name
        self.age = age
        self.health = health_level
        self.happines = happines_level

    def display_info(self):
        print(
            f"The {self.name} has {self.health} health and {self.happines} happiness."
        )

    def feed(self, amount=10):
        self.health += amount
        self.happines += amount


class Lion(Animal):

    def __init__(self, animal_name, age=1, pride_size=5):
        super().__init__(animal_name, age)
        self.pride_size = pride_size  # Unique attribute

    def feed(self, amount=30):
        super().feed(amount)  # Custom feeding behavior


class Tiger(Animal):

    def __init__(self, animal_name, age=1, stripe_pattern="Bold"):
        super().__init__(animal_name, age)
        self.stripe_pattern = stripe_pattern  # Unique attribute

    def feed(self, amount=25):
        super().feed(amount)


class Monkey(Animal):

    def __init__(self, animal_name, age=1, favorite_food="Banana"):
        super().__init__(animal_name, age)
        self.favorite_food = favorite_food  # Unique attribute

    def feed(self, amount=20):
        super().feed(amount)


class Zoo:

    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("Mohammad's Zoo")

zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()


nala = Lion("Nala", age=3)
nala.feed()
nala.display_info()


        