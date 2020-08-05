import string 

def word_count(s):
    # create dictionary
    count = {}
    # punctuation marks '''!()-[]{};:"\,<>./?@#!$%^&*_~'''
    punctuations = ('":;,.-+=/\\|[]{}()*^&')
    s.lower()
    for x in s: 
        if x in punctuations: 
            s = s.replace(x, "")     
   
    words = s.split()
    for w in words:
        p = w.lower()
        if p not in count:
            count[p] = 0
        count[p] += 1
    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))