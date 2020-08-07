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


# first count the letters , then calculate frequency
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

cipher = dict(zip(ciphered_keys, most_used_values))
# print(cipher)
# for key in ciphered_list:
#     for value in most_used_values:
#         cipher[key] = value
#         most_used_values.remove(value)
#         break
# create translation list
translation = []

translate_me = words.split()
# loop thu translation and decipher
for word in translate_me:
    new_word = ""
    for ch in word:
        if ch in cipher.keys():
            v = cipher[ch]
            new_word += v
    translation.append(new_word)

print(" ".join(translation).lower())