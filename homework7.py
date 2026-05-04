# 1

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"hi, im {self.name} and im {self.age} years old")


person1 = person("Zuka", 25)
person2 = person("Anna", 23)
person3 = person("Maka", 34)

person1.greet()
person2.greet()
person3.greet()


    
  
# 2
    

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        perimeter = 2 * (self.width + self.height)   
        return perimeter

    def is_square(self):
        if self.width == self.height:
            return True
        return False


rectangle1 = rectangle(7, 7)
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle1.is_square())   

rectangle2 = rectangle(12, 10)
print(rectangle2.area())
print(rectangle2.perimeter())
print(rectangle2.is_square())




       
# 3

class bankaccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"deposit: +${amount}")
        else:
            print("fail: amount must be positive")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"fail: balance is not enough for {amount}, balance: {self.balance} ")
        elif amount <= 0:
            print("amount must be positive")
        else:
            self.balance -= amount
            print(f"withdrow -${amount}. balance now>>>{self.balance}")
    def __str__(self):
        return f"account ({self.owner}): {self.balance}"
    


my_account = bankaccount("zuka", 100)
my_account.deposit(50)
my_account.withdraw(30)
my_account.withdraw(200)
print(my_account)



# 4


class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes sound.")

class dog(animal):
    def speak(self):
        print(f"dog {self.name} says woof!")

class cat(animal):
    def speak(self):
        print(f"cat {self.name} says meow!")

generic_animal = animal("some animal")
my_dog = dog("Loma")
my_cat = cat("Tedo")

animals = [generic_animal, my_dog, my_cat]
for animal in animals:
    animal.speak()




# 5 


class book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __repr__(self):
        return f"Book ({self.title}, {self.author}, {self.pages}p)"
    
    def __eq__(self, other: object):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
            
    def __len__(self):
        return self.pages
    
    book1 = Book("the great gatsby", "scott fitzgerald", 180)
    book2 = Book("the great gatsby", "scott fitzgerald", 208)
    book3 = Book("1984", "george orwell", 310)

    print(f"book 1: {book1}")
    print(f"book 3 pages {len(book3)}")
    print(f"book 1 is equal book 2: {book1 == book2}")
    print(f"book 1 is equal book 3: {book1 == book3}")
