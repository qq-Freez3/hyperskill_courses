import itertools
import time

def timecheck(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Function takes {round(end - start, 10)} seconds to run")
    return wrapper

def chain():
    list1 = [1, 2, 3]; list2 = [4, 5, 6]; list3 = [7, 8, 9]

    for num in itertools.chain(list1, list3, list2):
        print(num)

@timecheck
def small_product():
    first_list = ['Hi', 'Bye', 'How are you']
    second_list = ['Jane', 'Anton']

    for first, second in itertools.product(first_list, second_list):
        print(first, second)

@timecheck
def big_product():
    #cant_store_in_memory = list(itertools.product(range(1000000), range(1000000)))

    my_iterator = itertools.product(range(1000000), range(1000000))
    for i in range(10):
        print(next(my_iterator))

def wombo_combo():
    my_list = ["Pass", "The", "Rock", "Please"]
    iterator_boi = itertools.combinations(my_list, 2)
    #every combination of 2 values using values 1 - noninclusive 10
    #excluding duplicates like 1:1, 2:2, 3:3

    boss = lambda: print(next(iterator_boi))

    while True:
        try:
            boss()
        except StopIteration:
            break

def gather():
    all_students = ['Ann', 'Kate', 'Tom', 'Jane', 'Mike', 'Ann', 'Carl', 'Mike']

    all_students.sort()
    #groupby does not work without sorted list
    #each new item creates new key

    #key defaults to each unique name since no key was specified
    for key, group in itertools.groupby(all_students):
        print(key, list(group))

    shortboy = lambda x: len(x)
    all_students.sort(key=shortboy)

    #group by each unique length of names
    for key, group in itertools.groupby(all_students, key=shortboy):
        print(key, list(group))

if __name__ == '__main__':
    #chain() #concatenates list
    #small_product() #(x, y)(a, b, c) = xa, ab, ac, ya, yb, yc
    #big_product() #Cartesian product one by one
    #wombo_combo()
    gather()