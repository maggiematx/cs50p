# Ask user for their name
name=input("What's your name")

# Remove whitespace from str and capitalize user's name
name = name.strip()

# Capitalize user's name
name=name.title()


print(f'Hello,  {name}')

name=input("What's your name?").strip().title()