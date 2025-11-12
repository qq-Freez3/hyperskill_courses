import re

def your_name_please():
    """FirstName MiddleName? Smith"""

    arrow = r"([A-Z][a-z]+)(\s[A-Z][a-z]+)?\sSmith"
    hit = lambda target: print(re.match(arrow, target))

    hit("Chaz Smith") # pass successfully
    hit("Rhonda Rousey Smith") #pass successfully
    hit("smith Smith") #fail successfully
    hit("Dusty GabbaSmith") #fail successfully

def numbered_list():
    """ 1) Curiosity 2) Perseverance 3) ?
        1) cabbage 2) carrot 3) apple 4) oranges """

    arrow = r"^([0-9]+\)\s{1}[A-Za-z]+\s{1})*?([0-9]+\)\s{1}[A-Za-z]+)$"
    target = "1) cabbage 2) carrot 3) apple 4) oranges"
    hit = lambda x: print(re.match(arrow, x))
    hit(target)

if __name__ == '__main__':
    #your_name_please() #quantifiers module
    numbered_list() #groups and alternations module