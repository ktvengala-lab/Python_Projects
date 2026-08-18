# The user enters a sentence, and your program analyzes it.

sentence = input("Type your text here: ")

word = ""
repeat_words = 0
words_list = []
new_word = []

count_vowels = 0
count_characters = 0
count_words = 0
vowels_list = []

count_spaces = 0
count_consonant = 0
consonant_list = []

vowels = ["a", "e", "i", "o", "u"]

# Build words and analyze characters
for character in sentence:
    count_characters += 1

    if character != " ":
        word = word + character

    elif character == " ":
        if word != "":
            words_list.append(word)
            count_words += 1
            word = ""

    if character in vowels:
        count_vowels += 1
        vowels_list.append(character)

    elif character != " ":
        count_consonant += 1
        consonant_list.append(character)

    else:
        count_spaces += 1


# Add the final word
if word != "":
    words_list.append(word)
    count_words += 1


# Find repeated words
for each_word in words_list:
    repeat_words = 0

    for each_other_word in words_list:
        if each_word == each_other_word:
            repeat_words += 1

    if repeat_words > 1:
        if each_word not in new_word:
            new_word.append(each_word)


# Results
print()
print("========== TEXT ANALYZER ==========")
print()

print("Words:", words_list)
print("Repeated words:", new_word)
print("Vowels:", vowels_list)
print("Consonants:", consonant_list)

print()
print(f"The total number of consonants: {count_consonant}")
print(f"The total number of vowels: {count_vowels}")
print(f"The total number of words: {count_words}")
print(f"The number of spaces: {count_spaces}")
print(f"The number of characters: {count_characters}")