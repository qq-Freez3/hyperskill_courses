import itertools


def struggle_meals(max = 30):
    """ print meal combinations that don't exceed expected price
        ex: fried fish ice-cream cola 28 -and- fried fish cake cola 30 """

    main_courses = ['beef stew', 'fried fish']
    price_main_courses = [28, 23]

    desserts = ['ice-cream', 'cake']
    price_desserts = [2, 4]

    drinks = ['cola', 'wine']
    price_drinks = [3, 10]

    meal_product = []; price_product = []

    for course, dessert, drink in itertools.product(main_courses, desserts, drinks):
        meal_product.append(f'{course} {dessert} {drink}')
    #print(meal_product)

    for course_price, dessert_price, drink_price in itertools.product(price_main_courses, price_desserts, price_drinks):
        price_product.append(course_price + dessert_price + drink_price)
    #print(price_product)

    for foodish, priceish in zip(meal_product, price_product):
        print(foodish, priceish)

def large_population():
    """print all countries with a population over 100 million"""
    many_people = lambda x: x["population_mil"] <= 100 #why not >= ???
    countries = [{"name": "USA", "population_mil": 150}, {"name": "BFA", "population_mil": 21}, {"name": "FFA", "population_mil": 180}]
    countries.sort(key=many_people)

    for key, locations in itertools.groupby(countries, key=many_people):
        print(key, len(list(locations))) # 2 countries over or equal 100 in this list
        break

def flower_shop():
    """print every combination of bouquets ranging from 1 to 3 flowers per bouquet"""
    flower_names = ['rose', 'tulip', 'sunflower', 'daisy'] #test list

    jump = lambda x: itertools.combinations(flower_names, x)

    for wombo in jump(1):
        print(wombo)
    for wombo in jump(2):
        print(wombo)
    for wombo in jump(3):
        print(wombo)

def say_my_name():

    names = ["Jack", "Michael", "Jane", "Ann"]
    bookkeeper = lambda x: x[0]
    #names.sort(key=bookkeeper)
    names.sort()

    for key, name_set in itertools.groupby(names, key=bookkeeper):
        print(list(name_set))

if __name__ == '__main__':
    #struggle_meals()
    #large_population()
    #flower_shop()
    say_my_name()
