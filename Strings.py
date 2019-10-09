myStr = 'Hi Friend'
# restusn all options for string object
#print(dir(myStr)) 

print(myStr)

# converts strings in uppercase
print(myStr.upper())

#converts string in lowercase
print(myStr.lower())

#change lower to upper an viceverse
print(myStr.swapcase())

# convert the first character in strings to uppercase and the rest to lowercase
print(myStr.capitalize())

# replace a selected characfter or chain inside string by another chain or character
print(myStr.replace("Hi", "Bye"))

#you can make chain methods

print(myStr.replace("Hi", "Bye").swapcase())

#counts a character or chain of it
print(myStr.count('i'))

#checks if string starts with a character or a chain. Is case sensitive
print(myStr.startswith("Hi"))
print(myStr.startswith("hi"))

#the same as start width but in the end
print(myStr.endswith("friend"))
print(myStr.endswith("Friend"))

#sepataes a string base on spaces or characters
print(myStr.split())
myStr2 = 'Hi,Friend'
print(myStr2.split(','))
print(myStr2.split('i'))

#returns the index of character finded
print(myStr2.find('e'))

#returns the lenght of something
print(len(myStr))

#gets the index of the first character or a chain of it finded
print(myStr.index('Fr'))
print(myStr.index('i'))
print(myStr.index('d'))
print(myStr.index('Hi'))

#check if string ir character is numeric
print(myStr.isnumeric())
myStr3 = '789'
myStr4 = 'sdassdgfwerdf'
print(myStr3.isnumeric())

#check is is alphanumeric
print(myStr4.isalpha())

#pritns the character based on index
print(myStr[0])
print(myStr[-1])

#concatenation
print('message: ' + myStr)
print(f'message: {myStr}')