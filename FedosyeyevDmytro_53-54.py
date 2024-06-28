# Завдання 1
# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine
# (містить інформацію про кавомашину), клас Blender (містить інформацію про блендер), клас MeatGrinder
# (містить інформацію про м’ясорубку). Кожен із класів має містити необхідні для роботи методи.

class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power


    def get_info(self):
        return f'Brand: {self.brand}, Model: {self.model}, Power: {self.power}'


class CoffeMachine(Device):
    def __init__(self, brand, model, power, water_capacity):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity

    def made_coffe(self, sort_coffe):
        return f'Make a cup of {sort_coffe} coffee.'

    def get_info(self):
        return f'{super().get_info()}, Water capacity: {self.water_capacity}'

class Blender(Device):
    def __init__(self, brand, model, power, speed_settings):
        super().__init__(brand, model, power)
        self.speed_settings = speed_settings

    def blend(self, speed):
        return f'Blend with selected speed {speed}.'

    def get_info(self):
        return f'{super().get_info()}, Speed settings: {self.speed_settings}'

class MeatGrinder(Device):
    def __init__(self, brand, model, power, blade_material):
        super().__init__(brand, model, power)
        self.blade_material = blade_material

    def grind_meat(self, meat_type):
        return f"Grinding {meat_type} meat."

    def get_info(self):
        return f"{super().get_info()}, Blade Material: {self.blade_material}"

# Завдання 2
# Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас
# Frigate (містить інформацію про фрегат), клас Destroyer (містить
# інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер).
# Кожен із класів має містити необхідні для роботи методи.

class Ship:
    def __init__(self, name, displacement, max_speed, crew_size):
        self.name = name
        self.displacement = displacement
        self.max_speed = max_speed
        self.crew_size = crew_size

    def get_info(self):
        return f"Name: {self.name}, Displacement: {self.displacement} tons, Max Speed: {self.max_speed} knots, Crew Size: {self.crew_size}"

    def sail(self):
        return f"The ship {self.name} is sailing at {self.max_speed} knots."


class Frigate(Ship):
    def __init__(self, name, displacement, max_speed, crew_size, weapon):
        super().__init__(name, displacement, max_speed, crew_size)
        self.weapon = weapon

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Weapon: {self.weapon}"

    def anti_submarine_operations(self):
        return f"The frigate {self.name} is performing anti-submarine operations."


class Destroyer(Ship):
    def __init__(self, name, displacement, max_speed, crew_size, torpedoes):
        super().__init__(name, displacement, max_speed, crew_size)
        self.torpedoes = torpedoes

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Type of torpedo: {self.torpedoes}"

    def launch_torpedo(self):
        return f"The destroyer {self.name} is launching torpedo."


class Cruiser(Ship):
    def __init__(self, name, displacement, max_speed, crew_size, turret_guns):
        super().__init__(name, displacement, max_speed, crew_size)
        self.turret_guns = turret_guns

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Turret guns: {self.turret_guns}"

    def strike_operations(self):
        return f"The cruiser {self.name} is shoots from turret guns."


# Завдання 3
# Запрограмуйте клас Money (об’єкт класу оперує однією валютою) для роботи з грошима. У класі мають бути передбачені:
# поле для зберігання цілої частини грошей (долари, євро, гривні тощо) і поле для зберігання копійок
# (центи, євроценти, копійки тощо). Реалізуйте методи виведення суми на екран, задання значень частин.
# Створіть клас Product для роботи з продуктом або товаром беручи за основу клас Money. Реалізуйте метод для
# зменшення ціни на задане число. Для кожного з класів реалізуйте необхідні методи та поля.

class Money:
    def __init__(self, whole_part=0, coins=0):
        self.whole_part = whole_part
        self.coins = coins
        self.normalize()

    def normalize(self):
        if self.coins >= 100:
            self.whole_part += self.coins // 100
            self.coins = self.coins % 100
        elif self.whole_part < 0:
            self.whole_part, self.coins = 0, 0

    def display(self):
        return f"{self.whole_part}.{str(self.coins)}"

    def set_money(self, whole_part, coins):
        self.whole_part = coins
        self.coins = coins
        self.normalize()

    def subtract(self, other):
        new_whole = self.whole_part - other.whole_part
        new_coins = self.coins - other.coins
        result = Money(new_whole, new_coins)
        result.normalize()
        return result


class Product:
    def __init__(self, name, price_whole, price_coins):
        self.name = name
        self.price = Money(price_whole, price_coins)

    def display_price(self):
        return f"The price of {self.name} is {self.price.display()}"

    def reduce_price(self, reduction_whole, reduction_coins):
        reduction = Money(reduction_whole, reduction_coins)
        self.price = self.price.subtract(reduction)
        if self.price.whole_part < 0:
            self.price.whole_part, self.price.fractional_part = 0, 0
