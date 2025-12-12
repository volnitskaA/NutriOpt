from product import Product
from comparison import ComparisonService

p1 = Product("Product A", 40, 500, 600)
p2 = Product("Product B", 35, 400, 550)

products = [p1, p2]

service = ComparisonService()

best_price = service.compare_by_price(products)
best_calories = service.compare_by_calories(products)

print("Найвигідніший за ціною:", best_price.name)
print("Найвигідніший за калорійністю:", best_calories.name)

# main application file
