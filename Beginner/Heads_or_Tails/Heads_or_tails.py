import random

print("Welcome to the Heads or Tails Game!")
random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
print(random_heads_or_tails)
