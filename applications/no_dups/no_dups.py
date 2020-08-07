def no_dups(s):
    # set up dictionary
    singles = {}
    
    words = s.split()
    for w in words:
        singles[w] = w
    separator = ' '
    
    return separator.join(list(singles.values()))
    
    

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))