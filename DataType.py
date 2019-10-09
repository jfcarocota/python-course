#strings.
print("hello world")
print('hello world')
print("""hello world""")
print('''hello world''')

#show expression or variable type, ergo, you need print for seeing this, type cant show in console by itself.
print(type("hello world"))

#string concatenation
print("hello" + "world")

#sum by two numbers
print(4 + 5)

#variable type number
number = 4
print(type(number))

#contatenation mutiple examples.
print(f'hello{4}')
print(f'my number is: {number}')

# this will be a bool (need to be capital letter at first character)
print(type(False))
print(type(True))

#list. Lsits can be toitally generic, can combine multiple values types.
arrList = [10, 5, 4, 3, 2, 'hello', 14.16, True] 
print(arrList)
print(type(arrList))

#tuples. They are constant, can be changed.
arrTuple = (10, 5, 4)
print(arrTuple)
print(type(arrTuple))

#Dinctionaries or the equivalent of objects in javascript (json). The first part is the Key, and the next is the value.
dictionary = {
    "name" : "John",
    "lastName" : "Doe",
    "nickname" : "jonny",
    "age" : 34,
    "gender" : "male"
}

print(dictionary)
print(type(dictionary))