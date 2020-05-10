from sys import argv
liked_numbers = argv[1].split("-")
disliked_numbers = argv[2].split("-")
given_numbers = argv[3].split("-")
happiness = 0
for num in given_numbers:
    if num in liked_numbers:
        happiness += 1
    if num in disliked_numbers:
        happiness -= 1
print(happiness)