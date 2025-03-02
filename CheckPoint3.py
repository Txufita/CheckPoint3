
# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
Dog_Name = "Txufi the best dog"
Age = 4
Preferences = ["eating", "playing", "biting", "running"]
Will_drive_you_crazy = True
# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable. 
first_three_letters = Dog_Name[0:3]
print(first_three_letters)
# Exercise 3: Use an index to grab the first element from your list
first_element = Preferences[0]
print(first_element)
# Exercise 4: Create a new number variable that adds 10 to your original number
new_number = Age + 10
print(new_number)
# Exercise 5: Use an index to get the last element in your list.
last_element = Preferences[-1]
print(last_element)
# Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list)
# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.

first_word = Dog_Name[0:4]
print(first_word.upper())
new_string = first_word.upper() + Dog_Name[4:]
print(new_string)
# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print(f"I have {new_number} years old")
# Exercise 9: Print “hello world”.
print("hello world")
# YAdemás necesito que me crees una cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena con "adiós".
string = "Hello"
print(string.replace("Hello", "bye"))






