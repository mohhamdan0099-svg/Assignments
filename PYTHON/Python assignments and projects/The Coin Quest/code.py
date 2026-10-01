class Backpack:
    def __init__(self, owner, coins=0):
        self.owner = owner
        self.coins = coins

    def add_coins(self, amount):
        self.coins += amount

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
        else:
            print("Not enough coins")
        return self

    def display(self):
        print(f"{self.owner}'s backpack has {self.coins} coins")
        return self

class Hero:
    def __init__(self, name):
        self.name = name
        self.backpack = Backpack(name)

    def collect(self, amount):
        # Fixed: Hero does not have a direct coins attribute; we must modify the associated Backpack object.
        self.backpack.add_coins(amount)
        return self

    def buy_item(self, amount):
        self.backpack.spend_coins(amount)
        return self

    def gift_coins(self, other_hero, amount):
        if self.backpack.coins >= amount:
            # Fixed: Deduct coins from self before giving them to other_hero
            self.backpack.spend_coins(amount)
            other_hero.backpack.add_coins(amount)
        return self

# Verification
hero1 = Hero("Lina")
hero2 = Hero("Omar")

hero1.collect(50).buy_item(15).gift_coins(hero2, 20)

hero1.backpack.display()
hero2.backpack.display()