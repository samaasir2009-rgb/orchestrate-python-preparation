name='samaasir'
language='python'
college='Muchhala polytechnic college'

print(name)
print(language)
print(college)




x="python"
print(type(x))



name="python"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])


word="programming"
print(word[1:4])

word="anantharaj"
print(word[:3])
print(word[2:])
print(word[:])




word="samu xavior"
print(word.upper())
print(word.lower())
print(word.title())
print(len(word))


fruite=("apple","bannana","grapes")
print(fruite)
print(fruite[0])
print(fruite[1])
print(fruite[2])
fruite=list(fruite)
fruite.append("orange")
fruite=tuple(fruite)
print(fruite)
fruite=list(fruite)
fruite.remove("bannana")
print(fruite)




number=[10,20,30]
number.insert(1,15)
print(number)


number=(10,20,30,40)
number=list(number)
number.pop(1)
print(number)


number=(50,60,30,20,70,100)
number=list(number)
number.reverse()
print(number)



number=(10,20,30,40)
number=list(number)
number.reverse()
print(number)




number=(10,20,30,40)
number=list(number)
number.pop()
number.append(50)
print(number)



name = "Python"
numbers = [2, 4, 6]

numbers.append(8)

print(name[0:3])
print(numbers[2])
print(len(numbers))