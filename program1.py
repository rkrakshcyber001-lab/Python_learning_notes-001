"""
#Program 1

print("hello World")

#Program 2

print("hello \nworld") #usage of escape sequence

# Program 3

print("Hey", end="009") 
print("Hello")

# Program 4

print("hey", 4,sep="*") #o/p: hey*4


# Program 5
a=2
b=4

print(f"addition of the two numbers {a} and  {b}:",a+b )
print(f"subtraction of the two numbers {a} and  {b}:",a-b )
print(f"multiplication of the two numbers {a} and  {b}:",a*b )
print(f"division of the two numbers {a} and  {b}:",a/b )


# Program 6
a = "1"
b = "2"
print(int(a) + int(b)) # Type Casting - explicit conversion (user manually does the type casting)

# Program 7

a = 7.6 #float
b = 4   #int
c=a+b

print(c) #float cz its implicit conversion did by the python interpreter to carry out the operation based on the order level of data type
print(type(a))
print(type(b))
print(type(c))

# Program 8  
a = int(input("enter the 1st number:"))
b = int(input("enter the 2nd number:"))
print(a + b)

# Program 9 - Accessing characters of a string
name = "raksha"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Program 10 - Looping through string
name = "kamala"
for character in name:
    print(character)

# Program 11 - Finding the length of a string
container = "boxing"
print(f"the length of the word {container} is" ,len(container))

# Program 12 - Slicing of characters in a string
string_slicing = "HappyBirthday" #for slicing the indexing will take the inputs from 0 to n-1
print(string_slicing[0:5])
print(string_slicing[:5]) # python will automatically consider the index from 0 without mentioning it
print(string_slicing[5:14])
print(len(string_slicing))
print(string_slicing[:]) # prints the whole string
print(string_slicing[0:len(string_slicing)-8])
print(string_slicing[0:-8]) #negative slicing
print(string_slicing[-8:-3]) # output: Birth
"""

# Program 13 - String methods and operations (Strings are immutable)
instrument = "Fluteeeeee"
print(instrument.upper())
print(instrument.lower())
print(instrument.rsplit('t')) # it removes the character mentioned from the right side
print(instrument.replace('F','B'))
print(instrument.capitalize())
print(len(instrument))
print(len(instrument.center(25)))
print(instrument.count('e'))
print(instrument.endswith('e'))
print(instrument.endswith('eee',7,10))
stationary = "glue is so sticky and works as a good adhesive"
household = "     "
print(stationary.find('is')) # gives the index of the first occurrence of the mentioned character
print(stationary.index('is'))
print(household.isalnum()) # checks if the string has only alphabets and numbers
print(household.isalpha()) # checks if the string has only alphabets
print(household.islower()) # checks if the string has only lowercase letters
print(household.isupper()) # checks if the string has only uppercase letters
print(household.isspace()) # checks if the string has only spaces
print(stationary.startswith('g')) # checks if the string starts with the mentioned character
print(stationary.startswith('s',9,11)) # checks if the string starts with
print(stationary.strip()) # removes the extra spaces in the starting and ending of the string
print(stationary.swapcase()) # converts uppercase to lowercase and vice versa
print(stationary.title()) # converts the first letter of each word to uppercase