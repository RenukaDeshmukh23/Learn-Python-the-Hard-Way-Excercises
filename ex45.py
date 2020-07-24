from sys import exit
from random import randint
from textwrap import dedent

class Start(object):
    def enter():
        print(dedent("""Choose a path for you:
            left\t right\t straight
            """))
    def path():
        ch = input(">")
        if ch == "left":
            print("You have to cross a river..!!")
            print("r u hungry")
            food=River.eat()
        elif ch == "right":
            print("You will see many trees..!!")
            food=Tree.eat()
        else:
            print("Keep Moving..!!")

class Food(object):
    def eat():
        print("\t Y \t N")
        ch = input(">")
        if ch == 'Y':
            print("Eat all the fruits")
        else:
            print("Keep Moving...")

class River(Start,Food):
    def __init__(self):
        self.food=Food()

class Tree():
    def eat():
        print("\t Y \t N")
        ch = input(">")
        if ch == 'Y':
            print("eat bananas")
        elif ch == 'N':
            print("Eat vegetables")
        else:
            print("You are not hungry")

class Jungle(object):
    start = Start.enter()
    start = Start.path()
