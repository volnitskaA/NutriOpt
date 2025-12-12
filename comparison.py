class ComparisonService:
    def compare_by_price(self, products):
        return min(products, key=lambda p: p.price_per_100g())

    def compare_by_calories(self, products):
        return max(products, key=lambda p: p.calories_per_uah())
