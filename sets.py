from sets_categories_data import (ALCOHOLS)


def clean_ingredients(dish_name, dish_ingredients):
    dish_ingredients = set(dish_ingredients)
    return (dish_name, dish_ingredients)
#print(clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']))


def check_drinks(drink_name, drink_ingredients):
    for ingredient in ALCOHOLS:    
        if ingredient in drink_ingredients:
            return f'{drink_name} Mocktail'
        else:
            return f"{drink_name} Cocktail"
#print(check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber']))
#print(check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda']))
