# Ask user for their name
name=input("What's your name")

# Remove whitespace from str and capitalize user's name
name = name.strip()

# Capitalize user's name
name=name.title()

print(f'Hello,  {name}')

name=input("What's your name?").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")
print(f"hello, {first}")


x=int(input("what's x?"))
y=int(input("what's y?"))
print (x+y)


x=float(input("what's x?"))
y=float(input("what's y?"))
print(round(x+y))