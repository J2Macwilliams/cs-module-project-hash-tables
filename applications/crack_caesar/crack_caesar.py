# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
# pull in text an make possible to read
with open("applications/crack_caesar/ciphertext.txt") as f:
    words = f.read()
countwords = words


# symbols to remove
symbols = '!()-[]{};:"\,<>./?@#!$%^&*_~'

for x in countwords: 
    if x in symbols: 
        countwords = countwords.replace(x, "")

# remove spaces to find total of all letters
totalWords = len("".join(countwords.split()))


# first count the letters 
letters = {}
# create list of words
just_letters = countwords.split()

# loop thru the text and find the count for the letters
for word in just_letters:
    for ch in word:
        if ch not in letters:
            letters[ch] = 0
        letters[ch] +=1

letters_sorted = sorted(letters.items(), key=lambda x: x[1], reverse=True)
# calculate the frequency
frequency = {}

for pair in letters_sorted:
    list(pair)
    total = float(totalWords)
    lcount = float(pair[1])
    percentage = '{0:.2f}'.format(lcount / total * 100)
    frequency[pair[0]] = percentage

# gather from readMe most used letters
most_used_values = ['E','T','A','O','H','N','R','I','S','D','L','W','U','G','F','B','M','Y','C','P','K','V','Q','J','X','Z']
# most frequent letters in cipher in list
ciphered_keys = list(frequency.keys())
# join two lists into dictionary
cipher = dict(zip(ciphered_keys, most_used_values))

# create new phrase string
deciphered_phrase=''
# loop thru the old phrase and decipher
for l in words:
    if l in cipher.keys():
        l = cipher[l]
        deciphered_phrase += l
    else:
        deciphered_phrase += l
       

print(deciphered_phrase)
