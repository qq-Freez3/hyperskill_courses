def basic_iterator():
    my_list = [1, 2, 3]
    my_iterator = iter(my_list)
    print(my_iterator) #an iterator is like a for or while loop

    #just look
    just_do_it = lambda: print(next(my_iterator))

    try:
        for i in range(6): just_do_it()
    except StopIteration:
        print("End of the line\n")

def zip_it():
    first_names = ['John', 'Anna', 'Tom', "Boob", "Beverly", "Bashful", "Blamey"]
    last_names = ['Smith', 'Williams', 'Davis']

    for name, last_name in zip(first_names, last_names):
        print(name, last_name)
    #--------------------------------#
    boss_iterator = iter(zip(first_names, last_names))
    since_when = lambda: print(next(boss_iterator))

    try:
        for i in range(len(first_names)): since_when()
    except StopIteration:
        print("Which one of yall?\n")
    #------------------------------------#
    failed_iterator = iter(zip(first_names, last_names, strict=True))
    will_it_fail = lambda: print(next(failed_iterator))

    for i in range(len(last_names)): will_it_fail()

    try:
        will_it_fail()
    except ValueError:
        print("List 1 was longer than list 2")
        print(("Boob", None))

def make_it_clap():
    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    enumerator = enumerate(months_list, start=1) #start makes changes index from 0
    print(next(enumerator))
    print(next(enumerator))

    for n, month in enumerator:
        print(n, month)

def samp_vectors():
    """return sum of coordinates for each vector"""
    v1 = (1, 8, 9)
    v2 = (7, 5, 8)

    zipper = iter(zip(v1, v2))

    for i, n in zipper:
        print(i + n)

def play_with_strings(let1, let2):

    zipper = iter(zip(let1, let2))
    new_word = ''

    for i, n in zipper:
        new_word += (i + n)

    print(new_word)

if __name__ == "__main__":
    #basic_iterator()
    zip_it()
    #make_it_clap() #enumerate
    #samp_vectors()
    #play_with_strings("mo", "ew")
    #play_with_strings("age", "lake")