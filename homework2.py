#1
name = input("whats your name?")
print(name.upper())
print(name.lower())
print(name.title())



#2
sentence = "  the quick brown fox jumps over the lazy dog  "

stripped_sentence = sentence.strip()
print(stripped_sentence)

count_o = sentence.count("o")
print(count_o)

replaced = sentence.replace("fox", "cat")
print(replaced)

words = stripped_sentence.split()
first3 = words[:3]
print(first3)







#3
age = int(input("whats your age?"))
if age < 13:
    print("you are child")
elif 13 <= age <= 17:
    print("you are teenager")
elif 18 <= age <= 64:
    print("you are adult")
else:
    print("you are senior")



#4
username = input("Username>>> ")
password = input("password>>> ")
correct_username = "admin"
correct_password = "secret"

if username != correct_username:
    print("user not fount")
if username == correct_username and password == correct_password:
    print("welcome, admin")
if username == correct_username and password != correct_password:
    print("incorrect password")



#5
age = int(input("whats your age?"))
status = input("are you student? (yes/no)")
student = status == "yes" and 12 <= age
children = age < 12
adults = 18 <= age <= 64 != status
senior = 65 <= age

if children:
    print("Ticket price: 5$")
elif student:
    print("Ticket price: 8$")
elif adults:
    print("Ticket price: 15$")
else:
    print("Ticket price: 10$")
