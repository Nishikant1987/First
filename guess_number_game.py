import random as r

a = r.randint(1, 100)
user = int(input("enter a number of your choice: "))
count = 0

while(a != user):
    count += 1
    if (user<a):
        user=int(input("enter a higher number: "))
    elif(user>a):
        user=int(input("print a lower number: "))


print("you have guessed the correct number in {} attempts".format(count))
         