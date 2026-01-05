# print("hello world!")

# name = input("enter your name :")
# age = int(input("enter your age:"))

# print("hello" ,name)
# if(age>18):
#     print("you can apply for license")
# else:
#     print("you are not applicable.")


# name = input("enter name :")
# curr_year = int(input("enter current year:"))
# birth_year = int(input("enter your birth year:"))

# age = curr_year - birth_year 
# print(age)


# def split_bill(amount,people):
#     if(people > 1):
#         per_person = amount / people
#     elif(people < 0):
#         print("something is wrong")
#         return 0
#     else:
#         per_person =  amount
#     return per_person

# amount = float(input("enter amount:"))
# people = int(input("enter people:"))


# result = split_bill(amount, people)
# print(result)

# name = input("enter your name :")
# age = int(input("enter your age:"))

# print("my name is", name ,"and i am" ,age ,"years old")

class Animal:
    def speak(self):
        return "I am an animal."

class Dog(Animal):
    def speak(self):
        return "Woof!"

print(Dog().speak())

class Cat:
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    # This function works for both Dog and Cat because they both have a 'speak' method.
    return animal.speak()

print(make_animal_speak(Cat()))
print(make_animal_speak(Dog()))





