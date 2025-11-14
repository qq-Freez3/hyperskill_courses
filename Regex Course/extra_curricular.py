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

def phone_number():
    target = input("Number: ")
    # your code here
    arrow = r"\+(\d{1})[-\s]{,1}(\d{3})[-\s]{,1}(\d{3}[-\s]{,1}\d{2}[-\s]{,1}\d{2})$"
    hit = re.match(arrow, target)

    if hit is not None:
        print(f"Full number: {hit.group()}")
        print(f"Country code: {hit.group(1)}")
        print(f"Area code: {hit.group(2)}")
        print(f"Number: {hit.group(3)}")
    else:
        print("No match")

def posthumously():
    """ AM I supposed to be using a post-condition here???
        I still got the right result
        https://hyperskill.org/learn/step/14258 """

    target = input()
    # your code here
    arrow = r"([\w\s]+ \$(\d+),?)+$"

    hit = re.compile(arrow)
    if hit.match(target) is not None:
        chances = target.split(",")
        # print(chances) test successful

        sum = 0
        for chance in chances:
            sum += int(hit.match(chance).group(2))
        print(f"This week you have spent: {sum} dollars")

def webdev():
    """print list of items contained within
        html tags <li> (example) </li>"""

    target = "<li>Sister</li> <li>Father</li> <li>Mother-in-law</li>"
    arrow = r"(?<=<li>)[-\w\s]+(?=</li>)"

    hit = re.compile(arrow)
    captured = hit.findall(target)

    for i in captured:
        print(i)

if __name__ == '__main__':
    #your_name_please() #quantifiers module
    #numbered_list() #groups and alternations module
    #phone_number() #groups and alternations module
    #posthumously() #Jesus #Preconditions and Post Conditions
    webdev() #Preconditions and Post Conditions