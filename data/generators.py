import random
from faker import Faker

fake = Faker('ru_RU')

def generate_user_registration_data():
    data = {'email': fake.email(), 'password': fake.password(), 'name': fake.first_name()}
    return data

def generate_user_invalid_login_data():
    data = {'login': fake.email(), 'password': fake.password()}
    return data

def get_random_ingredients(count):
  if count > len(Ingridients.INGRIDIENTS):
    raise ValueError('Заданное количество превышает размер списка ингредиентов!')
  return random.sample(Ingridients.INGRIDIENTS, count)