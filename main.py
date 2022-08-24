# Magic 8 Ball
# Spencer Carlson


import random

name = "Spencer" # Name of person using the Magic 8-Ball.
question = "Will it rain today?" # Question the person is asking the Magic 8-Ball.
answer = ""

random_number = random.randint(1,10) # Choosing random number between 1-10.

# Possible answers below.

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell me now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Not a chance."
else:
  answer = "Error"

# This section will print the answer or tell you what information is missing.

if name == "":
  print("I need to know your name.")
elif question == "":
  print("I need to know your question.")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)