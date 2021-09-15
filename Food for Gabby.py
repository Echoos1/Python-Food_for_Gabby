import random

clear = "\n" * 100

# Import Text Files
foods = open('foods.txt').read().splitlines()

def gen():
    print(clear, random.choice(foods))
    prompt()


def prompt():
    retry = input("\nPress ENTER to Choose Another\n")
    gen()

gen()
prompt()
