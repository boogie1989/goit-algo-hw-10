# Імпорт необхідних бібліотек
from pulp import LpMaximize, LpProblem, LpVariable

# Створення моделі
model = LpProblem(name="beverage-production", sense=LpMaximize)

# Визначення змінних
lemonade = LpVariable(name="lemonade", lowBound=0,
                      cat='Integer')  # кількість "Лимонаду"
# кількість "Фруктового соку"
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat='Integer')

# Формулювання цільової функції
model += lemonade + fruit_juice, "Total number of products"

# Додавання обмежень
model += (2 * lemonade + 1 * fruit_juice <=
          100), "Water Constraint"  # обмеження на "Воду"
model += (1 * lemonade <= 50), "Sugar Constraint"  # обмеження на "Цукор"
# обмеження на "Лимонний сік"
model += (1 * lemonade <= 30), "Lemon Juice Constraint"
# обмеження на "Фруктове пюре"
model += (2 * fruit_juice <= 40), "Fruit Puree Constraint"

model.solve()

print(f"Production of Lemonade: {lemonade.varValue}")
print(f"Production of Fruit Juice: {fruit_juice.varValue}")
print(f"Total Products: {model.objective.value()}")


# Production of Lemonade: 30.0
# Production of Fruit Juice: 20.0
# Total Products: 50.0