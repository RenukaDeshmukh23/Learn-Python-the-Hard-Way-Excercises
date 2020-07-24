from sys import argv

script,user_name=argv
prompt='ANS:'

print(f"Hi {user_name},I'm the {script} script.")
print("I'd like to ask you few questions.")
print(f"DO you like me {user_name}?")
likes=input(prompt)

print(f"where do you live {user_name}?")
lives=input(prompt)

print(f"what kind of a computer do you have")
computer=input(prompt)

print(f"""
alright, so u said {likes} about liking me.
You live in {lives} .
and you have a computer {computer}.
""")
