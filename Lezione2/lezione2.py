# Alessandro Vitale 18/04/24

print('Hello world')

# 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

# questa variabile contiene il nome
name: str = 'Mario'

#questa variabile contiene il messaggio
message: str = f'Ciao {name}, ti va di imparare un po di python insieme?'

print(message)

# 2-4. Name Cases: Use a variable to represent a person’s name, 
# and then print that person’s name in lowercase, uppercase, and title case.

# questa è una variabile che contiene il nome di una persona
name: str = 'Mario'

# questa variabile minuscolo
name_lower: str = name.lower()

#questa variabile maiuscolo
name_upper: str = name.upper()

# print(f"{name}, {name.upper()}, {name.lower()}")
print(f'{name}, {name_upper}, {name_lower}')

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks: Albert Einstein once said, 
# “A person who never made a mistake never tried anything new.”

name: str = 'Scherlock Holmes'

cit: str = 'una volta disse,"Elementare Watson"'

print(f'{name}, {cit}')

# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
# Assign the value 'python_notes.txt' to a variable called filename. 
# Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename: str = 'python_notes.txt'
print(filename.removesuffix('txt'))

# 3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

names: list = ['Mario', 'Luca', 'Franco']
for name in names:
    print(name)

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name.

names: list = ['Mario', 'Luca', 'Franco']
for name in names:
    print(f'Ciao {name}, ti va di prendere un caffè?')

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples.
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

mode_of_transport: list = ['Ferrari', 'Pagani', 'Honda']
for mode_of_transport in mode_of_transport:
    print(f'I would like to own a {mode_of_transport}')

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guest_list: list = ['Franco', 'Ugo', 'Chiara', 'Pluto']
for name in guest_list:
    print(f'Hi {name}, do you want come to dinner with me tonight?')

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.

print(f'{guest_list[0]} non può venire a cena')
print(f'{guest_list[3]} non può venire a cena')
guest_list.pop(0)
guest_list.insert(0, 'Maria')
guest_list.pop(3)
guest_list.insert(3, 'Franceca')
for name in guest_list:
    print(f'Hi {name}, do you want come...')

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

print(f'Hi {guest_list}, I found a bigger table')
guest_list.insert(0, 'Alex')
guest_list.insert(2, 'Maria')
guest_list.append('Pietro')
for name in guest_list:
    print(f'Hi {name}, we are a lot, come to dinner')

"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. 
  Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
  Print your list to make sure you actually have an empty list at the end of your program.
"""

print(f'Hi {guest_list}, I have a sit for only two people')
while len(guest_list)>2:
    name = guest_list.pop()
    print(f'Sorry {name}, you cant came')

print(f'{guest_list[0]} and {guest_list[1]}, you are still invited.')
del guest_list[-2:]

print(guest_list)

"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.
"""
# Egitto, Giappone, Norvegia, New York, Las Vegas

my_places: list = ['Egitto', 'Giappone', 'Norvegia', 'New York', 'Las Vegas']
print(sorted(my_places))
print(sorted(my_places, reverse = True))
my_places.reverse()
print(my_places)
my_places.reverse()
print(my_places)
my_places.sort()
print(my_places)
my_places.sort(reverse = True)
print(my_places)

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.
"""
guest_list: list = ['Franco', 'Ugo', 'Chiara', 'Pluto']
print(f'i am inviting {len(guest_list)} people to dinner')

"""
3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, 
or anything else you’d like. Write a program that creates a list 
containing these items and then uses each function introduced in this chapter at least once.
"""






