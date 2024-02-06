""" class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")

my_dog = Dog("willie", "6")
my_dog.sit()
my_dog.roll_over() """

""" class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.type}")

    def open_restaurant(self):
        print("The restaurant is now open.")

he_restaurant = Restaurant("The Great Feast", "Italian")
he_restaurant.describe_restaurant()
he_restaurant.open_restaurant() """

""" class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Cuisine type: {self.type}")

    def open_restaurant(self):
        print("The restaurant is now open.")

    def lai_number(self):
        print(f"lai de ren shu wei :{self.number_served}")

    def set_number_served(self, number_customers):
        self.number_served += number_customers

    def incerment_number_served(self, additional_customers):
        self.number_served += additional_customers

he_restaurant = Restaurant("The Great Feast", "Italian")
he_restaurant.describe_restaurant()
he_restaurant.open_restaurant()
he_restaurant.lai_number()

estimated_customers = 150
he_restaurant.incerment_number_served(estimated_customers)
he_restaurant.lai_number() """

""" class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

user1 = User("John", "Doe", 25, "New York")
user1.describe_user()
user1.greet_user()
print()

user2 = User("Alice", "Smith", 30, "London")
user2.describe_user()
user2.greet_user()
print()

user3 = User("Emma", "Johnson", 35, "Paris")
user3.describe_user()
user3.greet_user() """

""" class User:
    def __init__(self, first_name, last_name, age, location, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("John", "Doe", 25, "New York")
print(f"Initial login attempts: {user.login_attempts}")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Updated login attempts: {user.login_attempts}")

user.reset_login_attempts()
print(f"Reset login attempts: {user.login_attempts}") """

""" class Rrstaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Rrstaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [ ]

    def show_flavors(self):
        if self.flavors:
            print(f"Ice Cream Flavors at {self.restaurant_name}:")
            for flavor in self.flavors:
                print(f"- {flavor}")
    
        else:
            print("No ice cream flavors available.")

my_ice_cream_stand = IceCreamStand("The Frosty Scoop", "Ice Cream")
my_ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chip"]
my_ice_cream_stand.show_flavors() """

""" class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.username}!")

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin privileges:")
        for priviege in self.privileges:
             print(f"- {priviege}")

admin = Admin("John", "Doe", "johndoe", "johndoe@example.com")
admin.show_privileges() """

""" class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.module = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        
        else:
            print("You can't roll back the odometer!")

    def increment_odometer(self, mils):
        self.odometer_reading += mils

class Battery:
    def __init__(self, battery_size = 60):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 60:
            mileage_range = 140

        elif self.battery_size == 85:
            mileage_range = 185
        
        else:
            mileage_range = 0

        print(f"This car can go approximately {mileage_range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
        
class ElectriCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_electr_car = ElectriCar("Tesla", "Model S", 2022)
my_electr_car.battery.get_range()
my_electr_car.battery.upgrade_battery()
my_electr_car.battery.get_range() """

