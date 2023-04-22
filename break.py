
av=5
x = int(input("How much candies do u want "))
i=1
while i<=x:
    if i>av:
        print("out of stock")
        break

    print("candy")
    i = i + 2
print("bye")