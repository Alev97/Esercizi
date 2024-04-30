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


"""
4-5. Summing a Million: Make a list of the numbers from one to one million,
 and then use min() and max() to make sure your list actually starts at one and ends at one million. 
 Also, use the sum() function to see how quickly Python can add a million numbers.
"""

numbers = list(range(1,1000001))
for number in numbers:
    minnums = min(numbers)
    maxnums = max(numbers)
    sumnums = sum(numbers)
print(minnums)
print(maxnums)
print(sumnums)


"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list
 of the odd numbers from 1 to 20. Use a for loop to print each number.
"""

oddnums = list(range(1,21,4))
for nums in oddnums:
    print(nums)

"""
4-7. Threes: Make a list of the multiples of 3, from 3 to 30.
 Use a for loop to print the numbers in your list.
"""

multiples_of_3 = list(range(3,31,3))
for nums in multiples_of_3:
    print(nums)

"""
4-8. Cubes: A number raised to the third power is called a cube.
 For example, the cube of 2 is written as 2**3 in Python.
 Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10),
 and use a for loop to print out the value of each cube.
"""

cubenums = list(range(1,11))
for nums in cubenums:
    cube = nums ** 3
    print(cube)

"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
"""

cube = [nums ** 3 for nums in range(1,11)]
print(cube)

"""
4-10. Slices: Using one of the programs you wrote in this chapter, 
      add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:.
  Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. 
  Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. 
  Then use a slice to print the last three items in the list.
"""

# NON HO CAPITO CHE DEVO FARE

"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:,
 and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, 
 and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
"""

my_favpizza = ['Margherita','Patate','Capricciosa']
friend_pizza = my_favpizza[:]
my_favpizza.append('Crostino')
friend_pizza.append('Marinara')
for pizza in my_favpizza:
    print(f'My favourite pizza are: {pizza}')
for pizza in friend_pizza:
    print(f"My friend's pizza are: {pizza}")

"""
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing,
 to save space. Choose a version of foods.py, and write two for loops to print each list of foods.
"""

# NON HO CAPITO

"""
4-15. Code Review: Choose three of the programs you’ve written in this chapter
 and modify each one to comply with PEP 8.
"""
# CONTINUO A NON CAPIRE

"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""

pet = 'cat'
print("\nIs pet == 'cat'? I predict True")
print(pet == 'cat')
print("\nIs pet == 'dog'? I predict False")
print(pet == 'dog')

anime = 'dragon ball'
print("\nIs anime == 'dragon ball'? I predict True")
print(anime == 'dragon ball')
print("\nIs anime == 'johnny bravo'? I predict False")
print(anime == 'johnny bravo')

pizza = 'margherita'
print("\nIs pizza == 'margherita'? I predict True")
print(pizza == 'margherita')
print("\nIs pizza == 'ortolana'? I predict False")
print(pizza == 'ortolana')

pasta = 'carbonara'
print("\nIs pasta == 'carbonara'? I predict True")
print(pasta == 'carbonara')
print("\nIs pasta == 'aglio...'? I predict False")
print(pasta == 'aglio...')

sport = 'sci'
print("\nIs sport == 'sci'? I predict True")
print(sport == 'sci')
print("\nIs sport == 'volleyball'? I predict False")
print(sport == 'volleyball')

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
 Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. 
If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails.
 (The version that fails will have no output.)
"""

alien_color = 'red'
if alien_color == 'red':
    print('You earned 5 points')
if alien_color == 'green':
    print('You earned 5 points')

"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.

"""

alien_color = 'red'
if alien_color == 'red':
    print("You earned 5 points for shooting the alien.")
else:
    print("You earned 10 points for shooting the alien.")

alien_color = 'green'
if alien_color == 'red':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points for shooting the alien!")

"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""

alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting the yellow alien!")
else:
    print("You earned 15 points for shooting the red alien!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting the yellow alien!")
else:
    print("You earned 15 points for shooting the red alien!")

alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points for shooting the green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting the yellow alien!")
else:
    print("You earned 15 points for shooting the red alien!")
