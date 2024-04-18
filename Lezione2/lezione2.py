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


