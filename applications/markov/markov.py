import random



# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words

cache = {}
ends = '.?!'

my_list = words.split()

for i in range(len(my_list) - 1):
    word= my_list[i ]
    next_word = my_list[i + 1 ]

    if word not in cache:
        cache[word] = [next_word]
    else:
        cache[word].append(next_word)

startwords = []
stop_signs = "?.!"
for key in cache.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        startwords.append(key)

# TODO: construct 5 random sentences
# Your code here

stopped = False
count = 0
while count < 5:
    # for initial start word
    if count is 0:
        word = random.choice(startwords)
    print(word, end=" ")

    # chose a random following word
    if word[-1] in ends or len(word) > 1 and word[-2] in ends:
        # stopped = True
        count += 1
    
    # choose a random following word
    following = cache[word]

    word = random.choice(following)