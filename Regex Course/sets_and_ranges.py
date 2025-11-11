import re

def sets():
    """ meta characters [?.] inside sets(brackets) are regular
        escape right brackets \\] and backslashes \\ """

    arrow = '[bd]a[td]'
    boob = lambda target: print(re.match(arrow, target))
    boob("bat"); boob("tab"); boob("dad")

    arrow = r'¯[\\]_'
    boob(r'¯\_(ツ)_/¯')

def ranges():
    """ match only works for beginning of sub-string """
    print(re.match('[0-9][0-9]', '991'))
    print(re.match('love [a-zA-Z][0-9]', 'love U2'))
    print(re.match('[^A-Z]ance', 'Dance'))
    print(re.match('[^E-Z]ance', 'Dance'))

if __name__ == '__main__':
    #sets()
    ranges()