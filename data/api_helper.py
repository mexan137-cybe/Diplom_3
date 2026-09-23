import random
import requests
from data.config import ApiUrl  

def get_ingredients_by_types():
    url = ApiUrl.BASE_URL + ApiUrl.INGRIDIENTS
    response = requests.get(url)
    data = response.json()
    buns_dict = {}
    sauces_dict = {}
    mains_dict = {}
    for item in data["data"]:
        item_type = item["type"]
        item_name = item["name"] 
        if item_type == "bun":
            buns_dict[item_name] = item
        elif item_type == "sauce":
            sauces_dict[item_name] = item
        elif item_type == "main":
            mains_dict[item_name] = item
    return buns_dict, sauces_dict, mains_dict

def get_one_ingredients_of_each_type():
    buns, sauces, mains = get_ingredients_by_types()
    bun = buns[list(buns.keys())[0]]
    sauce = sauces[list(sauces.keys())[0]]
    main = mains[list(mains.keys())[0]]
    return [bun, sauce, main]

def generate_random_burger_data():  
    buns, sauces, mains = get_ingredients_by_types()
    random_bun_name = random.choice(list(buns.keys()))
    random_bun_obj = buns[random_bun_name]
    random_sauce_names = random.sample(list(sauces.keys()), random.randint(1, 2))
    random_main_names = random.sample(list(mains.keys()), random.randint(1, 2))
    random_sauce_objects = [sauces[name] for name in random_sauce_names]
    random_main_objects = [mains[name] for name in random_main_names]
    api_ingredients_ids = ([random_bun_obj["_id"]] + [item["_id"] for item in random_main_objects] + [item["_id"] for item in random_sauce_objects] + [random_bun_obj["_id"]])
    return {
        "bun": random_bun_obj,  
        "sauces": random_sauce_objects,  
        "mains": random_main_objects,  
        "api_payload": {"ingredients": api_ingredients_ids}
        }

def create_order_via_api(user_token: str) -> str:
    
    burger_data = generate_random_burger_data()
    payload = payload = burger_data["api_payload"]
    headers = {"Authorization": user_token}
    response = requests.post(ApiUrl.BASE_URL + ApiUrl.ORDER_URL, json=payload, headers=headers)
    res_data = response.json()
    if not res_data.get("success"):
        raise Exception(f"Не удалось создать заказ через API: {res_data}")
    return str(res_data["order"]["number"])