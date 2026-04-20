# 1 greeting



def Greet():
    print(f"hello {name}")

name = input("what's your name? ")
Greet()



# 2 math function


def Area():
    print(f"Area is {area}")
    print(f"Circumference is {circum}")
    print(f"Circle info: Area {area}, Circumference {circum}")

Radius = int(input("enter circle radius "))
circum = 2 * Radius * 3.14159
area = Radius * Radius * 3.14159
Area()



# 3 list statistics


def list_stats():
    print(f"sum is {total}")
    print(f"average is {average}")
    print(f"smallest number is {smallest}")
    print(f"largest number is {largest}")

numbers = [10, 25, 3, 47, 18, 32, 6]
total = sum(numbers)
average = sum(numbers) / len(numbers)
smallest = min(numbers)
largest = max(numbers)
list_stats()


# 4 word counter


def count_words():
    print(f"number of words is {num_words}")
    print(f"number of characters is {num_characters}")
    print(f"longest word is {longest}")

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
num_words = len(words)
num_characters = len(sentence)
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word
        
           
count_words()



# 5 grade calculator
 

grades = [92, 85, 67, 74, 55, 91, 80]


for grade in grades:
    if 90 <= grade <= 100:
        print(f"score: {grade} -> A")
    elif 80 <= grade <= 89:
        print(f"score: {grade} -> B")
    elif 70 <= grade <= 79:
        print(f"score: {grade} -> C")
    elif 60 <= grade <= 69:
        print(f"score: {grade} -> D")
    else:
        print(f"score: {grade} -> F")








# 6  password generator


import random

def generate_password(length=12, use_digits=True, use_uppercase=True):
    abc = "abcdefghijklmnopqrstuvwxyz"

    if use_uppercase == True:
        abc = abc + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if use_digits == True:
        abc = abc + "0123456789"
    password = ""

    for i in range(length):
        char = random.choice(abc)
        password = password + char
    
    return password

print(generate_password())
print(generate_password(8))
print(generate_password(16, use_digits = False))


