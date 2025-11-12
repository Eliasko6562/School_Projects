'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

'''
Slovník cars
----------------------------------------------------------------------------------------------------------
brands                  models                        years  fuel      automatic colors
----------------------------------------------------------------------------------------------------------
(Ford, Tesla, Toyota)   [Mustang, Model S, Corolla]   1964   [gasoline, diesel]  True      ['red', 'blue', 'white']
----------------------------------------------------------------------------------------------------------
Počet záznamů: 3

cars = {
    "brands": ("Ford", "Tesla", "Toyota"),
    "models": ["Mustang", "Model S", "Corolla"],
    "year": {1964, 2020, 2015},
    "fuel": ["gasoline", "diesel"],
    "automatic": True,
    "colors": ["red", "blue", "white"]
}

cars['weight'] = [1500, 2000, 1800]
del cars['fuel']

print(f'\nSlovník cars')
print('-' * 120)
print(f'          brands                          models                         year       automatic        colors')
print('-' * 120)
print(f'{cars["brands"]}   {cars["models"]}   {cars["year"]}   {cars["automatic"]}   {cars["colors"]}')
print('-' * 120)
'''

cars = {
  "car1": {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "features": ("V8", "rear-wheel"),  # tuple
    "colors": ["red", "blue"],        # list
    "safety_ratings": {5, 4}             # set
  },
  "car2": {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2020,
    "features": ("electric", "autopilot"),
    "colors": ["white", "black"],
    "safety_ratings": {5}
  },
  "car3": {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2015,
    "features": ("economy",),
    "colors": ["blue", "grey"],
    "safety_ratings": {4, 5}
  }
}

cars["car4"] = {
  "brand": "Honda",
  "model": "Civic",
  "year": 2018,
  "features": ("efficient",),
  "colors": ["silver", "black"],
  "safety_ratings": {5}
}

removed = cars.pop("car2")

print("\nSlovník cars (vnořený)\n")
print("id\tbrand\tmodel\tyear\tfeatures\tcolors\tsafety")
print("-" * 80)

for car, info in cars.items():
  features = ", ".join(info.get("features")) if isinstance(info.get("features"), (list, tuple)) else str(info.get("features"))
  colors = ", ".join(info.get("colors")) if isinstance(info.get("colors"), list) else str(info.get("colors"))
  safety = ", ".join(str(x) for x in sorted(info.get("safety_ratings", [])))
  print(f"{car}\t{info.get('brand','')}\t{info.get('model','')}\t{info.get('year','')}\t{features}\t{colors}\t{safety}")

print("-" * 80)
print(f"Počet záznamů: {len(cars)}")
print(f"(Odstraněno car2: {removed['brand']} {removed['model']})")

