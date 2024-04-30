"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list,
 and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, 
instead of printing just the name of the pizza. For each pizza, 
you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza.
 The output should consist of three or more lines about the kinds of pizza you like and then
   an additional sentence, such as I really love pizza!
"""

my_favpizza = ['Margherita','Patate','Capricciosa']
# for pizza in my_favpizza:
    # print(pizza)
for pizza in my_favpizza:
    print(f'I like {pizza} pizza')

print(f'I really love pizza')

"""
4-2. Animals: Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common.
 You could print a sentence, such as Any of these animals would make a great pet!
"""

animals = ['Tiger','Bat','Shark']
# for animal in animals:
   # print(animal)
for animal in animals:
    print(f'{animal} is a mammalian animal')

print('All these animals are carnivores')

# DA FINIRE

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
"""

for numbers in range(1,21):
    print(numbers)

"""
4-4. One Million: Make a list of the numbers from one to one million, 
and then use a for loop to print the numbers.
 (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
"""

numbers = list(range(1,1000001))
for number in numbers:
    print(number)


