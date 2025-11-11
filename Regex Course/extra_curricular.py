import re

def your_name_please():
    """FirstName MiddleName? Smith"""

    arrow = "[A-Z][a-z]+\s[A-Z]?[a-z]*?\s?Smith"
    hit = lambda target: print(re.match(arrow, target))

    hit("Chaz Smith")
    hit("Rhonda Rousey Smith")
    hit("smith Smith")
    hit("Dusty GabbaSmith") #fail, retry


if __name__ == '__main__':
    your_name_please() #quantifiers module