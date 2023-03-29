import random

with open("fuck.txt", "w") as f:
    for i in range(20):
        f.write(str(random.randint(0, 100)) + "\n")
