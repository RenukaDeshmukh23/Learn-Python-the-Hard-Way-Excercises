from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured..!!")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            current_scene.enter()

class Death(Scene):
    quips = [
        "You died. You kinda suck at this"
        "Your mom would be proud..!!"
        "Such a luser.!"
        ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothons of planet percel #25
        have invaded your ship ,and destroyed your entire crew.
        You are last survivivg member..

        Yor're running down the central corridor to the weapons armory
        when a Gothon jumps ouyt,.He's blocking The door.
        """))

        action = input("> ")

        if action == "Shoot!":
            print(dedent("""
        Quick on the draw you yank out blaster and fire it at the Gothon.
        His clown costume is flowing and moving around.
        """))
            return 'death'

        elif action == 'dodge!':
            print(dedent("""
        Like a workd class boxer you dodge.gothon stops and eats you..
        """))
            return 'death'
        elif action == 'tell a joke':
            print(dedent("""
        Lucky for you they made u learn..
        then jump thriugh weapon armory..!!
        """))
            return 'lase_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'Central_corridor'

class LaserWeaponArmy(Scene):
    def enter(self):
        print(dedent("""
        You do a dive role in weapon armory. crouch and scan the room for Gothons.
        If you get to code wrong then 10times then lock closes forever and you
        can't get the bomb.
        """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]>")
        guesses = 0
        while guess!= code and guesses <10:
            print("BBZZEEDD!")
            guesses += 1
            guess = input ("[keypad]>")
        if guess == code:
            print(dedent("""
            the container clicks open and seal breaks,letting gas out.
            You grab the neutron bomb around run as fast as you can
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            the lock buzzes one last time and then you hear
            a sicking melting sound as the machansm is fused
            """))
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the netron destruct bomb
        under your arm and surprises 5 Gonthon who are trying to
        take control of the ship.
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
            In a panic you know the bomb at the group of Ganthons
            and make a leap for the door.You die nowling they will
            probably blow up when it goes off.
            """))
            return 'death'
        elif action == "slowly place the bomb":
            print(dedent("""
        you point ur blaster at the bomb. now that the bomb is placed you run
        to the escape pod to get off this tin can.
        """))
            return 'escape_pod'
        else:
            print("DOES not COMPUTE")
            return "the_bridge"

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
        You rush to ship desperately trying it to escape before the whole
        ship explodes..You get to the chamber with escapepods nad now need one
        to take
               """))
        god_pod = randint(1,5)
        guess = input("[pod #]>")

        if int(guess)!= god_pod:
            print (dedent("""You jump into the pod {guess} and hit the eject
            button.The pod escape out in the void space,crushing your body
            into jam jelly
            """))
            return 'death'
        else:
            print(dedent(""" You jump into the pod{guess} and hit the eject button
            You won!!!!
            """))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("Upu won!! Good job!!")
        return 'finished'

class Map(object):

    scenes = {
    'Central_corridor':CentralCorridor(),
    'lase_weapon_armory':LaserWeaponArmy(),
    'the_bridge':TheBridge(),
    'escape_pod':EscapePod(),
    'death':Death(),
    'finished':Finished(),
    }
    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('Central_corridor')
a_game = Engine(a_map)
a_game.play()
