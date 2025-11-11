import re

def your_name_please():
    """FirstName MiddleName? Smith"""

    arrow = "([A-Z][a-z]+)(\\s[A-Z][a-z]+)?\\sSmith"
    hit = lambda target: print(re.match(arrow, target))

    hit("Chaz Smith") # pass successfully
    hit("Rhonda Rousey Smith") #pass successfully
    hit("smith Smith") #fail successfully
    hit("Dusty GabbaSmith") #fail successfully


if __name__ == '__main__':
    your_name_please() #quantifiers module