1 fav five movies

movies = ["blue mountains", "pulp fiction", "kill bill", "django", "inglourious basterds"]
print(movies[0], movies[-1])

# movies.append("interstellar")
# print(movies)

movies.insert(1, "interstellar")
print(movies)

movies.remove("django")
print(movies)

final_list = movies
print(final_list)





2

numbers = []
for i in range(5):
    num = int(input("enter 5 random number: "))
    numbers.append(num)
print(numbers)
print(sum(numbers))





3 even and odd

even = []
odd = []
for i in range(1, 21):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even:", even)
print("odd:", odd)







4 password checker

correct_password = "python123"
attempts = 0
while True:
    password = input("enter password>> ")

    if password == correct_password:
        print("access granted!")
        break
    else:
        attempts += 1
        print("wrong password, try again.")
    if attempts == 3:
        print("account locked!")
        break






5 multiplication table

number = int(input("enter random number>>"))
for i in range(1, 11):
   print(f"{number} x {i} = {number * i}")





6 word analyzer


letters = ["a", "e", "i", "o", "u"]
sentence = input("enter sentence>>>")
for letter in letters:
    print(letter, sentence.count(letter))
