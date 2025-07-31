
#Alternative Problem

#You start with a telomere of length L (in arbitrary units).
#Each cell division shortens the telomere by S units.
#You want to find out after how many divisions the telomere becomes too short (less than or equal to T units).



import matplotlib.pyplot as plt


#🔢 Input:
#L = initial telomere length (e.g. 100)

telLenght = 1000

#S = telomere loss per division (e.g. 5)

telLossPerDiv = 10

#T = threshold length when the cell stops dividing (e.g. 20)

divStopAt = 300


def telDiv(telLength, loss, stopAt):

    #“Take the current value of divisions, add 1 to it, and store the result back into divisions.”

    divisions = 0
    while telLength > stopAt:
        divisions += 1
        print(f"Cycle {divisions}: telomere = {telLength}")
        telLength -= loss

    print(f"No more divisions possible. Final telomere: {telLength}")
    print(f"Total divisions: {divisions}")
    return divisions

# Call like this:
telDiv(1000, 10, 300)


def telDiv(telLength, loss, stopAt):
    divisions = 0
    history = []

    while telLength > stopAt:
        divisions += 1
        history.append(telLength)
        telLength -= loss

    print(f"Total divisions: {divisions}")
    return history

# See telomere lengths per cycle
print(telDiv(100, 10, 50))


def telDiv(telLength, loss, stopAt):
    divisions = 0
    history = []

    while telLength > stopAt:
        divisions += 1
        history.append(telLength)
        telLength -= loss

    return history

history = telDiv(100, 10, 30)
plt.plot(range(1, len(history)+1), history)
plt.xlabel("Division Number")
plt.ylabel("Telomere Length")
plt.title("Telomere Shortening Over Time")
plt.grid(True)
plt.show()
