import re


def beginning_of_string():
    """Take note of double backslash"""
    target = "roads? where we're going we don't need roads."
    weird = lambda regex: re.match(regex, target)

    print(weird('roads\\?') is not None)
    print(weird('roads\\.') is not None)
    #print(re.match('roads\\?', target) is not None)

def any_part_of_string():
    target = "roads? where we're going we don't need roads."
    weird = lambda regex: print(re.search(regex, target))

    weird('roads\\?') #needs actual ?
    weird('roads\\.') #needs actual .
    weird('here')
    print(re.search("ROADS", target, flags=re.IGNORECASE))

def all_matches_of_string():
    """CHECK: re.finditer()"""

    target = "A million dollars isn’t cool. You know what’s cool? A billion dollars."

    weird = lambda regex, goto: print(re.findall(regex, goto))
    weird('[mb]illion', target)
    weird('thousand', target)

    target = '32 apples, 2 bananas, 5 pears, 10 strawberries'

    weird('(\\d+) (\\w+)', target) #\d+ == digit(s), \w+ == char(s) (+ means (s))
    weird('\\d+ \\w+', target)
    weird('(\\d+) \\w+', target)
    weird('\\d+ (\\w+)', target)

def splits_of_strings():
    target = '111412222234333345555544'
    print(re.split('4', target))
    print(re.split('4', target, maxsplit=2))

    target = "Roads? Where we're going we don't need roads."
    print(re.split('\\W+', target))

def substitute_strings():
    target = 'blue jeans, white shirt, yellow socks, white flower, blue black, yellow fish'
    pattern = '(blue|white|yellow|fish)'
    replacement = 'black'

    print(re.sub(pattern, replacement, target))
    print(re.sub(pattern, replacement, target, count=4))

def precompile_patterns():
    """you can skip the step of inputting the regex
    string in the re.match() and other functions"""

    target = "roads? where we're going we don't need roads."
    regexp = 'roads'
    re_ = re.compile(regexp)

    print(re_.match(target)) #print(re.match(regexp, target))
    print(re_.findall(target)) #print(re.findall(regexp, target))
    print(re_.split(target)) #print(re.split(regexp, target))
    print(re_.sub('cars', target)) #print(re.sub(regexp, 'cars', target))

def homework():
    # https://hyperskill.org/learn/step/14243
    # https://hyperskill.org/learn/step/14180





if __name__ == '__main__':
    #beginning_of_string()
    #any_part_of_string() #only returns first occurrence
    #all_matches_of_string()
    #splits_of_strings()
    #substitute_strings()
    #precompile_patterns()
    homework()