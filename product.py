class Product:
    def __init__(self, name, price, weight, calories):
        self.name = name
        self.price = price
        self.weight = weight
        self.calories = calories

    def price_per_100g(self):
        return (self.price / self.weight) * 100

    def calories_per_uah(self):
        return self.calories / self.price
