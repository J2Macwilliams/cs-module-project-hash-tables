

with open("applications/histo/robin.txt") as f:
    robin = f.read()


def count_hash(s):
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
            count[p] = ['#']
        count[p].append('#')

    return(count)

# tuple key value pairs
# sort pairs first by number of times they appear, then alphabetically
# create list from response
res = list(sorted(count_hash(robin).items(), key=lambda x: (-len(x[1]), x[0]  )))
# set up spacing variable
x= " "
# loop thru response
for item in res:
    print(f'{item[0]}{x:{10 - len(item[0])}}{"".join(item[1])}')



# decipher hints with rot13
#  .items() method on a dictionary might be useful.

#  it's possible for .sort() to sort on multiple keys at once.

#  negatives might help where reverse won't.

#  you can print a variable field width in an f-string with nested braces, like so {x:{y}}
