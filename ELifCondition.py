# n = int(input("Enter a number: "))
n = int(input())

if n%2 != 0:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
elif n >= 21:
    print("Not Weird")
else:
    print("Wrong input")
