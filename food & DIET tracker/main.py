def call(x, y):
    if x == 1 and y == 1:
        f = open("vasu_diet.txt", "a")
        abc = input("enter DIET here =>")
        f.write(abc)
        f.close()

    elif x == 1 and y == 2:
        f = open("vasu_food.txt", "a")
        abc = input("enter Food here =>")
        f.write(abc)
        f.close()

    elif x == 1 and y == 3:
        f = open("vasu_diet.txt")
        print(f.read())
        f.close()

    elif x == 1 and y == 4:
        f = open("vasu_food.txt")
        print(f.read())
        f.close()

    elif x == 2 and y == 1:
        f = open("rohan_diet.txt", "a")
        abc = input("enter DIET here =>")
        f.write(abc)
        f.close()

    elif x == 2 and y == 2:
        f = open("rohan_food.txt", "a")
        abc = input("enter Food here =>")
        f.write(abc)
        f.close()

    elif x == 2 and y == 3:
        f = open("rohan_diet.txt")
        print(f.read())
        f.close()

    elif x == 2 and y == 4:
        f = open("rohan_food.txt")
        print(f.read())
        f.close()

    elif x == 3 and y == 1:
        f = open("gopi_diet.txt", "a")
        abc = input("enter DIET here =>")
        f.write(abc)
        f.close()

    elif x == 3 and y == 2:
        f = open("gopi_food.txt", "a")
        abc = input("enter Food here =>")
        f.write(abc)
        f.close()

    elif x == 3 and y == 3:
        f = open("gopi_diet.txt")
        print(f.read())
        f.close()

    elif x == 3 and y == 4:
        f = open("gopi_food.txt")
        print(f.read())
        f.close()

    else:
        print("invalid choice")


member = ["vasu", "rohan", "gopi"]

print("select from here ")
i = 1

for item in member:
    print(i, " for ", item)
    i += 1

choice = int(input("enter your choice => "))

print("\n\nchouse anyone from here")
print("", "1 for add ", member[choice-1], "'s", "DIET", "\n", "2 for add ", member[choice-1], "'s", "Food",
      "\n", "3 for see ", member[choice-1], "'s", "DIET", "\n", "4 for see ", member[choice-1], "'s", "Food")
select = int(input("enter your choice here =>"))

call(choice, select)
