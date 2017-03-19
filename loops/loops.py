numbers = [1,2,3,4,5,10,4]

for item in numbers:
    print(item)


turkeys = ["john", "jacob", "jingle" ,"himmer","smith"]

for item in turkeys:
    print(item)



run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1