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