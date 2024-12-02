# Word Starting with a Given Letter
food=['pizza','cake','samosa','burger','vadapav']

letter = input('enter a letter : ')

for x in food:
    if x.startswith(letter):
        print(x)
        break

