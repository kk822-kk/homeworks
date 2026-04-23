1

grades = {
    "Zurab": 83,
    "Ana": 96,
    "Maka": 91,
    "Lasha": 79,
    "Tako": 88,
} 
   
for name, score in grades.items():
    print(f"{name}: {score}")

average = sum(grades.values()) / len(grades)
print(f"average: {average}")

best_student = max(grades, key=grades.get)
print(f"sightest-scoring student: {best_student}({grades[best_student]})")





2 


def count_letters(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    return counts
print(count_letters("hello world"))





3


def merge_lists(list1, list2):
    combined = list1.copy()
    for item, quantity in list2.items():
        if item in combined:
            combined[item] += quantity
        else:
            combined[item] = quantity
    return combined


list1 = {"milk": 2, "bread": 1, "eggs": 12}
list2 = {"milk": 1, "cheese": 1, "bread": 2}

print(merge_lists(list1, list2 ))







4 contact manager

contacts = []

def add_contacts(contacts_list, name, phone, email):
    new_contact = {"name": name, "phone": phone, "email": email}
    contacts_list.append(new_contact)

def find_by_name(contacts_list, name):
    for contact in contacts_list:
        if contact["name"] == name:
            return contact
    return None

def all_emails(contact_list):
    emails = []
    for contact in contact_list:
        emails.append(contact["email"])
    return emails

add_contacts(contacts, "giorgi", "555111", "giorgi@gmail.com")
add_contacts(contacts, "elene", "553331", "elene@gmail.com")
add_contacts(contacts, "lasha", "522111", "lasha@gmail.com")

print(f"found: {find_by_name(contacts, 'giorgi')}")
print(f"all emails: {all_emails(contacts)}")





5  


class_a = ["Inception", "Matrix", "Interstellar", "Joker"]
class_b = ["Matrix", "Titanic", "Joker", "Avatar", "Titanic"]


set_a = set(class_a)
set_b = set(class_b)

both = set_a.intersection(set_b)

only_one = set_a.symmetric_difference(set_b)

total_distinct = set_a.union(set_b)

print(f"both likes: {both}")
print(f"only one of them likes it: {only_one}")
print(f"total: {total_distinct}") 





#6

translator = {
    "hello": "გამარჯობა",
    "cat": "კატა", 
    "this": "ეს",
    "my": "ჩემი",
    "is": "არის",
    "big": "დიდი",
    "friend": "მეგობარი",
    "room": "ოთახი"
}

def translate(sentence, dictionary):
    words = sentence.split()
    translated_list = []

    for word in words:
        clean_word = word.lower()
        if clean_word in dictionary:
            translated_list.append(dictionary[clean_word])
        else:
            translated_list.append(word)

    return " ".join(translated_list)

result = translate("hello , this is my friend", translator)
print(result)





#7

emails = [
    "alice@x.com", 
    "john@x.com",  
    "giorgi@x.com",  
    "maka@x.com",  
    "giorgi@x.com",  
]

unique_emails = set(emails)
print(unique_emails)
print(f"Unique: {len(unique_emails)}, total: {len(emails)}")


