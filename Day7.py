def greet():
    print("Hello,python!")
greet()    


def greet(name):
    print("Hello",name)
greet("sam")


def add(a,b):
    return a + b
result= add(5,3)

print(result)




def check_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = check_number(12)
print(result)



def add(a,b):
    return a + b
result= add(15,25)

print(result)