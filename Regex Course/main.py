import re #necessary for regex

def a_match():
    regex = "hello"
    weird = lambda text: re.match(regex, text)
    print(weird("hellon") is not None) #match
    print(weird("henllo") is not None) #no match

def a_dot_match():
    regex = "meet. me.."
    weird = lambda text: re.match(regex, text)
    print(weird("meet5 me2?") is not None) #match
    print(weird("meetd_me\n") is not None) #no match

def a_question_match():
    regexp = '.? points? to gryffindor'

    # '.? points?' matches '1 point'
    re.match(regexp, '1 point to gryffindor')

    # '.? points?' matches '0 points'
    re.match(regexp, '0 points to gryffindor')

    # no match, since '.? points?' doesn't match '-5 points'
    re.match(regexp, '-5 points to gryffindor')

    # '.? points?' matches ' points'
    re.match(regexp, ' points to gryffindor')

def full_match_test():
    string_1 = 'I love Python 3'
    string_2 = 'i love Pitsaw'
    string_3 = 'we love Papuan'
    string_4 = 'we love php'

    regex = '..? love P..... ?.?'
    weird = lambda beach: re.match(regex, beach)

    print(weird(string_1) is not None)
    print(weird(string_2) is not None)
    print(weird(string_3) is not None)

def start_match_end():
    template = "100%?"
    string = "100% reason to remember the name"
    end_index = re.match(template, string).end()
    start_index = re.match(template, string).start()
    start_end = re.match(template, string).span()
    print("STart INdex", start_index)
    print(start_end)
    print(f"End INdex {end_index}{string[end_index:]}")

if __name__ == '__main__':
    #a_match()
    #a_dot_match()
    #a_question_match() #copy and paste from hyperskill
    #full_match_test()
    #start_match_end()
    pass